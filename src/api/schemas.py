from datetime import datetime

from pydantic import BaseModel


class SourceResponse(BaseModel):
    id: int
    name: str
    base_url: str
    is_active: bool
    created_at: datetime

    model_config = {"from_attributes": True}


class ArticleResponse(BaseModel):
    id: int
    source_id: int
    url: str
    title: str | None = None
    body: str | None = None
    scraped_at: datetime
    published_at: datetime | None = None

    model_config = {"from_attributes": True}


class CrawlJobResponse(BaseModel):
    id: int
    source_id: int
    status: str
    start_at: datetime | None = None
    end_at: datetime | None = None
    error_msg: str | None = None
    items_found: int

    model_config = {"from_attributes": True}


class PaginatedArticles(BaseModel):
    items: list[ArticleResponse]
    total: int
    page: int
    page_size: int
    has_next: bool

    model_config = {"from_attributes": True}
