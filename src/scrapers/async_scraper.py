import asyncio

import aiohttp

from src.parsers.parser import ParserStrategy
from src.repositories.repository import ArticleRepository
from src.scrapers.base_scraper import BaseScraper
from src.utils.retry import async_retry


class AsyncScraper(BaseScraper):
    def __init__(
        self,
        parser: ParserStrategy,
        repository: ArticleRepository,
        max_concurrent: int = 5,
    ):
        super().__init__(parser, repository)
        self._semaphore = asyncio.Semaphore(max_concurrent)

    @async_retry(max_attempts=3, base_delay=1.0)
    async def fetch(self, url: str) -> str:
        async with self._semaphore:
            async with aiohttp.ClientSession() as session:
                async with session.get(
                    url, timeout=aiohttp.ClientTimeout(total=10)
                ) as response:
                    response.raise_for_status()
                    return await response.text()

    async def run(self, url: str) -> None:
        html = await self.fetch(url)
        article = self._parser.parse(html, url)
        self._repository.save(article)

    async def run_many(self, urls: list[str]) -> None:
        tasks = [self.run(url) for url in urls]
        await asyncio.gather(*tasks, return_exceptions=True)
