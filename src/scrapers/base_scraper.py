from abc import ABC, abstractmethod

from src.parsers.parser import ParserStrategy
from src.repositories.repository import ArticleRepository


class BaseScraper(ABC):
    def __init__(self, parser: ParserStrategy, repository: ArticleRepository):
        self._parser = parser
        self._repository = repository

    def run(self, url: str) -> None:
        html = self.fetch(url)
        article = self._parser.parse(html, url)
        self._repository.save(article)

    @abstractmethod
    def fetch(self, url: str) -> str: ...
