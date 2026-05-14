from abc import ABC, abstractmethod

from src.models.article import Article


class ArticleRepository(ABC):
    @abstractmethod
    def save(self, article: Article) -> None:
        pass

    @abstractmethod
    def find_by_url(self, url: str) -> Article | None:
        pass

    @abstractmethod
    def find_all(self) -> list[Article]:
        pass


class InMemoryArticleRepository(ArticleRepository):
    def __init__(self):
        self._articles: list[Article] = []

    def save(self, article: Article) -> None:
        self._articles.append(article)

    def find_by_url(self, url: str) -> Article | None:
        for article in self._articles:
            if article.url == url:
                return article
        return None

    def find_all(self) -> list[Article]:
        return list(self._articles)
