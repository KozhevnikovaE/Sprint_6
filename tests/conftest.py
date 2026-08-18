
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from pages.main_page import MainPage

@pytest.fixture(scope="function")
def driver():
    options = Options()
    options.binary_location = r"C:\Users\ivank\AppData\Local\Mozilla Firefox\firefox.exe"
    # Чистый профиль для Firefox в Selenium 4
    from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
    profile = FirefoxProfile()
    options.profile = profile

    service = Service(GeckoDriverManager().install())
    driver = webdriver.Firefox(service=service, options=options)
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    main_page = MainPage(driver)
    main_page.open()
    main_page.accept_cookies()
    return main_page