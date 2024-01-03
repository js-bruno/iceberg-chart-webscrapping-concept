import os
import time
import pymongo
from src.core.use_case import GetAllTopics, GetAllCategoriesLinks
from src.core.domain.settings import load_settings

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def init_selenium() -> webdriver.Chrome:
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--headless")
    options.add_experimental_option(
        "prefs",
        {
            "profile.managed_default_content_settings.images": 2,
        },
    )
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    return browser


def run():
    browser = init_selenium()

    load_settings()
    get_all_topics_links_usecase = GetAllTopics(browser)
    get_all_gategories_links_usecase = GetAllCategoriesLinks(browser)

    topics_urls = get_all_topics_links_usecase.run()
    myclient = pymongo.MongoClient(os.getenv("MONGO_URL"))

    iceberg_db = myclient["iceberg"]
    category_col = iceberg_db["categories"]

    for topic in topics_urls:
        categories = get_all_gategories_links_usecase.run(topic.geturl())
        category_col.insert_many(categories)
        print(f"------------------ INSERTED topic: {topic.path} ------------------")


if __name__ == "__main__":
    inicio = time.perf_counter()
    resultado = run()
    fim = time.perf_counter()
    tempo_total = fim - inicio

    print(f"Tempo total de execução: {tempo_total:.9f} segundos")
