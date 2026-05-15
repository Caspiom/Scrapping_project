import pytest
import pytest_asyncio

from src.db.engine import AsyncSessionLocal
from src.db.models import Source
from src.repositories.sqlalchemy_repo import SQLAlchemyRepo


@pytest.mark.asyncio
async def test_bulk_upsert():
    async with AsyncSessionLocal() as session:
        async with session.begin():
            source = Source(name="G1", base_url="https://g1.globo.com/")
            session.add(source)
            await session.flush()
            repo = SQLAlchemyRepo(session)
            await repo.bulk_upsert(
                [
                    {
                        "url": "https://g1.com/noticia-1",
                        "title": "G1",
                        "source_id": source.id,
                    }
                ]
            )
            await repo.bulk_upsert(
                [
                    {
                        "url": "https://g1.com/noticia-1",
                        "title": "G1Novo",
                        "source_id": source.id,
                    }
                ]
            )
            artigo = await repo.find_by_url(url="https://g1.com/noticia-1")
            assert artigo is not None
            assert artigo.title == "G1Novo"
