import pytest
from pages.login_page import LoginPage

EMAIL = "Issina_Akbota_31_567@ya.ru"
PASSWORD = "qwerty6"

@pytest.mark.login
def test_login_from_main_page(chrome, base_url):
    driver = chrome
    try:
        page = LoginPage(driver, base_url)
        page.open_main()
        page.click_main_login()
        page.login(EMAIL, PASSWORD)
        assert page.is_logged_in() is True
    finally:
        driver.quit()

@pytest.mark.login
def test_login_from_cabinet_button(chrome, base_url):
    driver = chrome
    try:
        page = LoginPage(driver, base_url)
        page.open_main()
        page.click_cabinet()
        page.login(EMAIL, PASSWORD)
        assert page.is_logged_in() is True
    finally:
        driver.quit()

@pytest.mark.login
def test_login_from_registration_form(chrome, base_url):
    driver = chrome
    try:
        page = LoginPage(driver, base_url)
        page.open_register_and_click_login()
        page.login(EMAIL, PASSWORD)
        assert page.is_logged_in() is True
    finally:
        driver.quit()

@pytest.mark.login
def test_login_from_forgot_password(chrome, base_url):
    driver = chrome
    try:
        page = LoginPage(driver, base_url)
        page.open_forgot_and_click_login()
        page.login(EMAIL, PASSWORD)
        assert page.is_logged_in() is True
    finally:
        driver.quit()

