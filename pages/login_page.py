# pages/login_page.py
from pages.base_page import BasePage
from pages.locators import (
    MainPageLocators as M,
    CommonLocators as C,
    LoginPageLocators as L,
    RegistrationPageLocators as R,
    ForgotPasswordLocators as F,
)

class LoginPage(BasePage):
    PATH_MAIN = "/"
    PATH_LOGIN = "/login"
    PATH_REGISTER = "/register"
    PATH_FORGOT = "/forgot-password"

    def __init__(self, driver, base_url, timeout: int = 10):
        super().__init__(driver, base_url, timeout)

    # -------- Открытие страниц --------
    def open_main(self):
        self.open(self.PATH_MAIN)
        self.wait_clickable(M.MAIN_LOGIN_BUTTON)

    def open_login(self):
        self.open(self.PATH_LOGIN)
        self.wait_clickable(L.SUBMIT_LOGIN)

    def open_register_and_click_login(self):
        self.open(self.PATH_REGISTER)
        self.click(R.LINK_LOGIN_FROM_REGISTER)
        self.wait_clickable(L.SUBMIT_LOGIN)  # дождались формы входа

    def open_forgot_and_click_login(self):
        self.open(self.PATH_FORGOT)
        self.click(F.LOGIN_BUTTON)           # здесь именно кликаем
        self.wait_clickable(L.SUBMIT_LOGIN)  # и ждём форму входа

    # -------- Действия --------
    def click_main_login(self):
        self.click(M.MAIN_LOGIN_BUTTON)

    def click_cabinet(self):
        self.click(C.CABINET_BTN)

    def login(self, email: str, password: str):
        self.type(L.EMAIL_INPUT, email)
        self.type(L.PASSWORD_INPUT, password)
        self.click(L.SUBMIT_LOGIN)

    # -------- Проверки --------
    def is_logged_in(self) -> bool:
        self.wait_visible(M.MAKE_ORDER_BUTTON)  # «Оформить заказ» видна => вошли
        return True
