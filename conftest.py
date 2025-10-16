import pytest
from pages.registration_page import RegistrationPage

NAME = "Akbota"

@pytest.mark.registration
def test_successful_registration(chrome, base_url, gen_email, gen_password_valid):
    driver = chrome
    try:
        page = RegistrationPage(driver, base_url)
        page.open()
        email = gen_email()
        password = gen_password_valid()
        page.register(NAME, email, password)
        assert page.wait_success_redirect_to_login() is True
    finally:
        driver.quit()

@pytest.mark.registration
def test_error_on_short_password(chrome, base_url, gen_email, gen_password_short):
    driver = chrome
    try:
        page = RegistrationPage(driver, base_url)
        page.open()
        email = gen_email()
        short_pwd = gen_password_short()
        page.register(NAME, email, short_pwd)
        error_text = page.get_password_error_text()
        assert error_text != ""
        assert "Некорректный пароль" in error_text
    finally:
        driver.quit()
