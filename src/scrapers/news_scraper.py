import requests

from src.scrapers.base_scraper import BaseScraper


class NewsScraper(BaseScraper):
    def fetch(self, url: str) -> str:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
