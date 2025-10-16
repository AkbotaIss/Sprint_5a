from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import MainPageLocators as M
from pages.locators import CommonLocators as C
from pages.locators import LoginPageLocators as L
from pages.locators import RegistrationPageLocators as R
from pages.locators import ForgotPasswordLocators as F

class LoginPage:
    PATH_MAIN = "/"
    PATH_LOGIN = "/login"
    PATH_REGISTER = "/register"
    PATH_FORGOT = "/forgot-password"

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    def open_main(self):
        self.driver.get(self.base_url + self.PATH_MAIN)
        self.wait.until(EC.element_to_be_clickable(M.MAIN_LOGIN_BUTTON))

    def open_login(self):
        self.driver.get(self.base_url + self.PATH_LOGIN)
        self.wait.until(EC.element_to_be_clickable(L.SUBMIT_LOGIN))

    def open_register_and_click_login(self):
        self.driver.get(self.base_url + self.PATH_REGISTER)
        self.wait.until(EC.element_to_be_clickable(R.LINK_LOGIN_FROM_REGISTER)).click()

    def open_forgot_and_click_login(self):
        self.driver.get(self.base_url + self.PATH_FORGOT)
        self.wait.until(EC.element_to_be_clickable(F.LOGIN_BUTTON))

    def click_main_login(self):
        self.wait.until(EC.element_to_be_clickable(M.MAIN_LOGIN_BUTTON)).click()

    def click_cabinet(self):
        self.wait.until(EC.element_to_be_clickable(C.CABINET_BTN)).click()

    def login(self, email, password):
        self.wait.until(EC.visibility_of_element_located(L.EMAIL_INPUT)).send_keys(email)
        self.driver.find_element(*L.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*L.SUBMIT_LOGIN).click()

    def is_logged_in(self):
        from pages.locators import MainPageLocators as M2
        self.wait.until(EC.visibility_of_element_located(M2.MAKE_ORDER_BUTTON))
        return True
