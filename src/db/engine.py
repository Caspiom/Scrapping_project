from sqlalchemy.ext.asyncio import async_sessionmaker, create_async_engine

from src.db.models import Base

engine = create_async_engine("postgresql+asyncpg://postgres:postgres@localhost/crawler")
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
