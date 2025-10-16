from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import CommonLocators as C
from pages.locators import LoginPageLocators as L

class ConstructorPage:
    PATH_MAIN = "/"

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    def login_and_open_profile(self, email, password):
        self.driver.get(self.base_url + self.PATH_MAIN)
        self.wait.until(EC.element_to_be_clickable(C.CABINET_BTN)).click()
        self.wait.until(EC.visibility_of_element_located(L.EMAIL_INPUT)).send_keys(email)
        self.driver.find_element(*L.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*L.SUBMIT_LOGIN).click()
        self.wait.until(EC.url_contains("/account/profile"))

    def click_constructor(self):
        self.wait.until(EC.element_to_be_clickable(C.CONSTRUCTOR_BTN)).click()
        self.wait.until(EC.url_to_be(self.base_url + self.PATH_MAIN))
        return self.driver.current_url.endswith(self.PATH_MAIN)

    def click_logo(self):
        self.wait.until(EC.element_to_be_clickable(C.LOGO_LINK)).click()
        self.wait.until(EC.url_to_be(self.base_url + self.PATH_MAIN))
        return self.driver.current_url.endswith(self.PATH_MAIN)

