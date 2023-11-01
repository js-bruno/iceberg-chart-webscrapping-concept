import pymongo
from src.core.use_case import GetAllTopics, GetAllCategoriesLinks

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


def init_selenium() -> webdriver.Chrome:
    options = Options()
    options.add_argument("--incognito")
    options.add_argument("--headless")
    browser = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install()), options=options
    )
    return browser


if __name__ == "__main__":
    browser = init_selenium()
    get_all_topics_links_usecase = GetAllTopics(
        "https://icebergcharts.com/", browser
    )  # Chance to topic "get_all_topics_usecase"
    get_all_gategories_links_usecase = GetAllCategoriesLinks(browser)

    topics_urls = get_all_topics_links_usecase.run()
    # topics = []

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")
    iceberg_db = myclient["iceberg"]
    category_col = iceberg_db["categories"]

    for topic in topics_urls:
        categories = get_all_gategories_links_usecase.run(topic.geturl())
        for categorie in categories:
            id_line = category_col.insert_one(categorie.dict())
            print(f"(id:{id_line})INSERTED CATEGORIE: {categorie.name}")
