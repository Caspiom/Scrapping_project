from fastapi import APIRouter, BackgroundTasks, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from src.api.deps import get_db
from src.api.schemas import SourceResponse
from src.db.models import Source

router = APIRouter()


def fake_scraper(source_id: int): ...


@router.get("/sources", response_model=list[SourceResponse])
async def get_sources(db: AsyncSession = Depends(get_db)):
    result = await db.execute(select(Source))
    sources = result.scalars().all()
    return sources


@router.post("/{source_id}/scrape")
async def trigger_scrape(source_id: int, bg: BackgroundTasks):
    bg.add_task(fake_scraper, source_id)
    return {"message": "Scraper triggered", "source_id": source_id}
