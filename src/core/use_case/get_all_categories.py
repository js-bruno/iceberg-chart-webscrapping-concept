import time

from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

from src.core.domain import load_settings


class GetAllCategories:
    def __init__(self, url: str):
        self._url = url
        self._settings = load_settings()

    def run(self) -> list[str]:
        page_sourece = self._load_selenium_driver()
        page_bs = BeautifulSoup(page_sourece, "html.parser")
        categories = page_bs.find_all("a", class_="category")

        categories_urls = []
        for a_tag in categories:
            print(a_tag["href"])
            categories_urls.append(self._settings["ICEBERG_CHART_URL"] + a_tag["href"])

        return categories_urls

    def _load_selenium_driver(self) -> str:
        options = Options()
        options.add_argument("--incognito")
        options.add_argument("--headless")

        browser = webdriver.Chrome(
            service=ChromeService(ChromeDriverManager().install()), options=options
        )
        browser.get("https://icebergcharts.com/")
        time.sleep(2)
        return browser.page_source
