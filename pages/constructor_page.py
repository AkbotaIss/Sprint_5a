# pages/constructor_page.py
from pages.base_page import BasePage
from pages.locators import CommonLocators as C, LoginPageLocators as L, ProfilePageLocators as P


class ConstructorPage(BasePage):
    PATH_MAIN = "/"

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

    def open_main(self):
        """Открыть главную страницу"""
        self.open(self.PATH_MAIN)

    def login_and_open_profile(self, email, password):
        """Авторизация и переход в личный кабинет"""
        self.open_main()
        self.click(C.CABINET_BTN)
        self.type(L.EMAIL_INPUT, email)
        self.type(L.PASSWORD_INPUT, password)
        self.click(L.SUBMIT_LOGIN)
        self.wait_url_contains(P.PROFILE_URL_PART)
        return True

    def click_constructor(self):
        """Клик по 'Конструктор' и возврат на главную"""
        self.click(C.CONSTRUCTOR_BTN)
        self.wait_url_to_be(self.base_url + self.PATH_MAIN)
        return self.current_url().endswith(self.PATH_MAIN)

    def click_logo(self):
        """Клик по логотипу и возврат на главную"""
        self.click(C.LOGO_LINK)
        self.wait_url_to_be(self.base_url + self.PATH_MAIN)
        return self.current_url().endswith(self.PATH_MAIN)
