from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import CommonLocators as C
from pages.locators import LoginPageLocators as L
from pages.locators import ProfilePageLocators as P

class ProfilePage:
    PATH_MAIN = "/"
    PATH_LOGIN = "/login"

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    def open_main(self):
        self.driver.get(self.base_url + self.PATH_MAIN)
        self.wait.until(EC.element_to_be_clickable(C.CABINET_BTN))

    def click_cabinet_and_login(self, email, password):
        self.driver.find_element(*C.CABINET_BTN).click()
        self.wait.until(EC.visibility_of_element_located(L.EMAIL_INPUT)).send_keys(email)
        self.driver.find_element(*L.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*L.SUBMIT_LOGIN).click()

    def open_profile(self):
        self.wait.until(EC.url_contains(P.PROFILE_URL_PART))
        self.driver.find_element(*C.CABINET_BTN).click()
        self.wait.until(EC.url_contains(P.PROFILE_URL_PART))
        return True
