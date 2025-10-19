# pages/registration_page.py
from pages.base_page import BasePage
from pages.locators import RegistrationPageLocators as R
from pages.locators import LoginPageLocators as L


class RegistrationPage(BasePage):
    PATH_LOGIN = "/login"
    PATH_REGISTER = "/register"

    def __init__(self, driver, base_url, timeout: int = 10):
        super().__init__(driver, base_url, timeout)

    def open(self):
        """Открыть страницу регистрации"""
        self.open(self.PATH_REGISTER)
        if self.PATH_REGISTER not in self.current_url():
            self.open(self.PATH_LOGIN)
        self.wait_visible(R.SUBMIT_REGISTER)

    def register(self, name: str, email: str, password: str):
        """Заполнить форму регистрации"""
        self.type(R.NAME_INPUT, name)
        self.type(R.EMAIL_INPUT, email)
        self.type(R.PASSWORD_INPUT, password)
        self.click(R.SUBMIT_REGISTER)

    def wait_success_redirect_to_login(self) -> bool:
        """Ожидание успешного перехода на страницу входа"""
        self.wait_url_contains("/login")
        self.wait_visible(L.HEADER_LOGIN)
        return True

    def get_password_error_text(self) -> str:
        """Получить текст ошибки пароля (если есть)"""
        if self.exists(R.PASSWORD_ERROR):
            return self.get_text(R.PASSWORD_ERROR)
        return ""
