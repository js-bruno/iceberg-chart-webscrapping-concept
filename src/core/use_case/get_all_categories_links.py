import time
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
from src.core.domain.dto import CategoryEntryDTO, Iceberg

from src.core.domain import load_settings


class GetAllCategoriesLinks:
    def __init__(self, browser: Chrome):
        self._browser = browser
        self._settings = load_settings()

    def run(self, categorie_url: str) -> list[CategoryEntryDTO]:
        page = self._load_beautiful_soup(categorie_url)
        category_entrys = page.find_all("div", class_="categoryentry")
        for category in category_entrys:
            iceberg_urls = category.find_all("a")
            icebergs = []
            for i, iceberg in enumerate(iceberg_urls):
                complete_url = self._settings["ICEBERG_CHART_URL"] + iceberg["href"]
                icebergs.append(Iceberg(name=iceberg.text, url=complete_url))
                print(i, f"Found Iceberg:{iceberg.text}")

        yield CategoryEntryDTO(name=category.h4.text, icebergs=icebergs).dict()
        # return categorys

    def _load_beautiful_soup(self, url: str) -> BeautifulSoup:
        self._browser.get(url)
        time.sleep(2)
        return BeautifulSoup(self._browser.page_source, "html.parser")
