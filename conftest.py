import pytest, yaml
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
# не нашла что это такое, это не библиотека и в конспекте лекции про это ничего нету.
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]


@pytest.fixture(scope="session")
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install())
        options = webdriver.FirefoxOptions
        driver = webdriver.Firefox(service, options=options)
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions
        driver = webdriver.Chrome(service, options=options)
    yield driver
    driver.quit()
