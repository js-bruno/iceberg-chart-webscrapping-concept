import time
from selenium.webdriver import Chrome
from bs4 import BeautifulSoup
from src.core.domain.dto import CategoryEntryDTO, Iceberg


class GetAllCategoriesLinks:
    def __init__(self, browser: Chrome):
        self._browser = browser

    def run(self, categorie_url: str) -> list[CategoryEntryDTO]:
        page = self._load_beautiful_soup(categorie_url)
        category_entrys = page.find_all("div", class_="categoryentry")
        categorys = []
        for category in category_entrys:
            iceberg_urls = category.find_all("a")
            icebergs = []
            for iceberg in iceberg_urls:
                icebergs.append(Iceberg(name=iceberg.text, url=iceberg["href"]))

            category_dto = CategoryEntryDTO(name=category.h4, icebergs=icebergs)
            categorys.append(category_dto)
        return categorys

    def _load_beautiful_soup(self, url: str) -> BeautifulSoup:
        self._browser.get(url)
        time.sleep(2)
        return BeautifulSoup(self._browser.page_source, "html.parser")
