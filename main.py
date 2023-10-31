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
    get_all_categories_usecase = GetAllTopics(
        "https://icebergcharts.com/", browser
    )  # Chance to topic "get_all_topics_usecase"
    get_all_gategories_links_usecase = GetAllCategoriesLinks(browser)
    categories_url = get_all_categories_usecase.run()
    catego = []
    for topic in categories_url:
        teste = get_all_gategories_links_usecase.run(topic)
        print(teste)
    print(catego)
