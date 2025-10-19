# tests/test_registration.py
import time
import pytest
from pages.registration_page import RegistrationPage

NAME = "Akbota"
EMAIL = "Issina_Akbota_31_567@ya.ru"
PASSWORD_VALID = "qwerty6"
PASSWORD_SHORT = "12345"


@pytest.mark.registration
class TestRegistration:
    def test_successful_registration(self, chrome, base_url):
        """Проверка успешной регистрации с уникальным email"""
        page = RegistrationPage(chrome, base_url)
        page.open()
        unique_email = EMAIL.replace("@", f"+{int(time.time())}@")
        page.register(NAME, unique_email, PASSWORD_VALID)
        assert page.wait_success_redirect_to_login() is True

    def test_error_on_short_password(self, chrome, base_url):
        """Проверка ошибки при коротком пароле"""
        page = RegistrationPage(chrome, base_url)
        page.open()
        page.register(NAME, EMAIL, PASSWORD_SHORT)
        error_text = page.get_password_error_text()
        assert error_text != ""
        assert "Некорректный пароль" in error_text
