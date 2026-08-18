
import pytest
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service
from webdriver_manager.firefox import GeckoDriverManager

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