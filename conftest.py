# tests/conftest.py
import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(scope="session")
def base_url() -> str:

    return os.getenv("BASE_URL", "https://stellarburgers.education-services.ru")


@pytest.fixture
def chrome():

    options = ChromeOptions()
    # options.add_argument("--headless=new")   # при необходимости
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    try:
        yield driver
    finally:
        driver.quit()
