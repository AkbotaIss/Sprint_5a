# pages/profile_page.py
from pages.base_page import BasePage
from pages.locators import CommonLocators as C
from pages.locators import LoginPageLocators as L
from pages.locators import ProfilePageLocators as P


class ProfilePage(BasePage):
    PATH_MAIN = "/"
    PATH_LOGIN = "/login"

    def __init__(self, driver, base_url, timeout: int = 10):
        super().__init__(driver, base_url, timeout)

    def open_main(self):
        """Открыть главную страницу и дождаться кликабельности кнопки 'Личный кабинет'"""
        self.open(self.PATH_MAIN)
        self.wait_clickable(C.CABINET_BTN)

    def click_cabinet_and_login(self, email: str, password: str):
        """Перейти в личный кабинет и авторизоваться"""
        self.click(C.CABINET_BTN)
        self.type(L.EMAIL_INPUT, email)
        self.type(L.PASSWORD_INPUT, password)
        self.click(L.SUBMIT_LOGIN)

    def open_profile(self) -> bool:
        """Проверить переход в профиль"""
        self.wait_url_contains(P.PROFILE_URL_PART)
        self.click(C.CABINET_BTN)
        self.wait_url_contains(P.PROFILE_URL_PART)
        return True
