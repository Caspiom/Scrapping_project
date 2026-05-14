from abc import ABC, abstractmethod

from src.models.article import Article


class ParserStrategy(ABC):
    @abstractmethod
    def parse(self, html: str, url: str) -> Article:
        pass


class SimpleHTMLParser(ParserStrategy):
    def parse(self, html: str, url: str) -> Article:
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(html, "html.parser")
        title = soup.find("h1")
        title = title.get_text(strip=True) if title else "No title"
        content = soup.find("article") or soup.find("main") or soup.body
        content = content.get_text(strip=True) if content else ""
        return Article(url=url, title=title, content=content, source=url)
