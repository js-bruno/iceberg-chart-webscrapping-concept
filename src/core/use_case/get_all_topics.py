import time

from urllib.parse import urlparse
from bs4 import BeautifulSoup
from selenium.webdriver import Chrome

from src.core.domain import load_settings
from src.core.utils import format_url


class GetAllTopics:
    def __init__(self, browser: Chrome):
        self._browser = browser
        self._settings = load_settings()

    def run(self) -> list[str]:
        page = self._load_beautiful_soup()
        categories = page.find_all("a", class_="category")
        for a_tag in categories:
            iceberg_chart_url_domain = self._settings["ICEBERG_CHART_URL"]

            categorie_url_path = a_tag["href"]
            complete_url = "//" + iceberg_chart_url_domain + categorie_url_path

            parsed_url = urlparse(complete_url, "https")
            yield parsed_url

    def _load_beautiful_soup(self) -> BeautifulSoup:
        self._browser.get(format_url(self._settings["ICEBERG_CHART_URL"]))
        time.sleep(2)
        page_source = self._browser.page_source
        return BeautifulSoup(page_source, "html.parser")
