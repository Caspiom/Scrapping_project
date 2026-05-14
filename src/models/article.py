from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class Article:
    url: str
    title: str
    content: str
    source: str
    scraped_at: datetime = field(default_factory=datetime.now)
