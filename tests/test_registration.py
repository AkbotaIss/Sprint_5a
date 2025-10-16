import time
import pytest
from pages.registration_page import RegistrationPage

NAME = "Akbota"
EMAIL = "Issina_Akbota_31_567@ya.ru"

@pytest.mark.registration
def test_successful_registration(chrome, base_url):
    driver = chrome
    try:
        page = RegistrationPage(driver, base_url)
        page.open()
        unique_email = EMAIL.replace("@", f"+{int(time.time())}@")
        password = "qwerty6"
        page.register(NAME, unique_email, password)
        assert page.wait_success_redirect_to_login() is True
    finally:
        driver.quit()

@pytest.mark.registration
def test_error_on_short_password(chrome, base_url):
    driver = chrome
    try:
        page = RegistrationPage(driver, base_url)
        page.open()
        short_password = "12345"
        page.register(NAME, EMAIL, short_password)
        error_text = page.get_password_error_text()
        assert error_text != ""
        assert "Некорректный пароль" in error_text
    finally:
        driver.quit()

