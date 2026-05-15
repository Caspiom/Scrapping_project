from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert
from sqlalchemy.ext.asyncio import AsyncSession

from src.db.models import Article


class SQLAlchemyRepo:
    def __init__(self, session: AsyncSession):
        self._session = session

    async def find_by_url(self, url: str) -> Article | None:
        stmt = select(Article).where(Article.url == url)
        result = await self._session.execute(stmt)
        return result.scalar_one_or_none()

    async def save(self, article: Article):
        self._session.add(article)
        await self._session.flush()
        return article

    async def bulk_upsert(self, articles: list[dict]) -> int:
        stmt = insert(Article).values(articles)
        stmt = stmt.on_conflict_do_update(
            index_elements=["url"],
            set_={"title": stmt.excluded.title, "scraped_at": stmt.excluded.scraped_at},
        )
        result = await self._session.execute(stmt)
        return result.rowcount
