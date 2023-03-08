import pytest
from selenium import webdriver
from config.config import TestData


# Default fixture for webdriver with some extra settings
@pytest.fixture(params=["chrome"])
def init_driver(request):
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    # options.add_argument('--headless')
    options.add_argument("--window-size=1440x900")
    if request.param == "chrome":
        web_driver = webdriver.Chrome(executable_path=TestData.PATH)
        request.cls.driver = web_driver
        web_driver.maximize_window()
        yield
        web_driver.close()
