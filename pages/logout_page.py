# pages/logout_page.py
from pages.base_page import BasePage
from pages.locators import CommonLocators as C
from pages.locators import LoginPageLocators as L
from pages.locators import ProfilePageLocators as P


class LogoutPage(BasePage):
    PATH_MAIN = "/"
    PATH_LOGIN = "/login"

    def __init__(self, driver, base_url, timeout: int = 10):
        super().__init__(driver, base_url, timeout)

    def login_and_open_profile(self, email: str, password: str):
        """Открыть главную → перейти в ЛК → авторизоваться → дождаться профиля"""
        self.open(self.PATH_MAIN)
        self.click(C.CABINET_BTN)
        self.type(L.EMAIL_INPUT, email)
        self.type(L.PASSWORD_INPUT, password)
        self.click(L.SUBMIT_LOGIN)
        self.wait_url_contains(P.PROFILE_URL_PART)

    def click_logout(self) -> bool:
        """Клик 'Выход' → проверка редиректа на /login"""
        self.click(P.LOGOUT_BUTTON)
        self.wait_url_contains(self.PATH_LOGIN)
        return self.current_url().endswith(self.PATH_LOGIN)
