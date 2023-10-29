import time

from urllib.parse import urlparse
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome

from src.core.domain import load_settings


class GetAllCategories:
    def __init__(self, url: str, browser: Chrome):
        self._url = url
        self._browser = browser
        self._settings = load_settings()

    def run(self) -> list[str]:
        page = self._load_beautiful_soup()
        categories = page.find_all("a", class_="category")

        categories_urls = []
        for a_tag in categories:
            complete_url = self._settings["ICEBERG_CHART_URL"] + a_tag["href"]
            parsedUrl = urlparse(complete_url, "https")
            categories_urls.append(parsedUrl.geturl())

        return categories_urls

    def _load_beautiful_soup(self) -> BeautifulSoup:
        self._browser.get("https://icebergcharts.com/")
        time.sleep(2)
        page_source = self._browser.page_source
        return BeautifulSoup(page_source, "html.parser")
