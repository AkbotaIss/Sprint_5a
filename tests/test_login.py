# tests/test_login.py
import pytest
from pages.login_page import LoginPage

EMAIL = "Issina_Akbota_31_567@ya.ru"
PASSWORD = "qwerty6"


@pytest.mark.login
class TestLogin:
    def test_login_from_main_page(self, chrome, base_url):
        """Авторизация через кнопку 'Войти в аккаунт' на главной странице"""
        page = LoginPage(chrome, base_url)
        page.open_main()
        page.click_main_login()
        page.login(EMAIL, PASSWORD)
        assert page.is_logged_in() is True

    def test_login_from_cabinet_button(self, chrome, base_url):
        """Авторизация через кнопку 'Личный кабинет'"""
        page = LoginPage(chrome, base_url)
        page.open_main()
        page.click_cabinet()
        page.login(EMAIL, PASSWORD)
        assert page.is_logged_in() is True

    def test_login_from_registration_form(self, chrome, base_url):
        """Авторизация через форму регистрации"""
        page = LoginPage(chrome, base_url)
        page.open_register_and_click_login()
        page.login(EMAIL, PASSWORD)
        assert page.is_logged_in() is True

    def test_login_from_forgot_password(self, chrome, base_url):
        """Авторизация через страницу восстановления пароля"""
        page = LoginPage(chrome, base_url)
        page.open_forgot_and_click_login()
        page.login(EMAIL, PASSWORD)
        assert page.is_logged_in() is True
