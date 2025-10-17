import os
import uuid
import random
import string
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions


@pytest.fixture(scope="session")
def base_url():
    """Базовый адрес тестируемого сайта"""
    return os.getenv("BASE_URL", "https://stellarburgers.education-services.ru/")


@pytest.fixture
def chrome():
    """Фикстура для инициализации и закрытия браузера Chrome"""
    options = ChromeOptions()
    # options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def gen_email():
    """Генератор уникальных email-адресов"""
    def _make(prefix="Issina_Akbota_31_567", domain="ya.ru"):
        return f"{prefix}_{uuid.uuid4().hex[:6]}@{domain}"
    return _make


@pytest.fixture
def gen_password_valid():
    """Генератор валидных паролей"""
    def _make(length: int = 10):
        pool = string.ascii_letters + string.digits
        core_len = max(6, length)
        return "".join(random.choices(pool, k=core_len))
    return _make


@pytest.fixture
def gen_password_short():
    """Генератор слишком коротких паролей"""
    def _make():
        return "12345"
    return _make
