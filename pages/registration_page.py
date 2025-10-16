from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import RegistrationPageLocators as R
from pages.locators import LoginPageLocators as L

class RegistrationPage:
    PATH_LOGIN = "/login"
    PATH_REGISTER = "/register"

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.base_url + self.PATH_REGISTER)
        if self.PATH_REGISTER not in self.driver.current_url:
            self.driver.get(self.base_url + self.PATH_LOGIN)
        self.wait.until(EC.visibility_of_element_located(R.SUBMIT_REGISTER))

    def register(self, name, email, password):
        self.wait.until(EC.visibility_of_element_located(R.NAME_INPUT)).send_keys(name)
        self.driver.find_element(*R.EMAIL_INPUT).send_keys(email)
        self.driver.find_element(*R.PASSWORD_INPUT).send_keys(password)
        self.driver.find_element(*R.SUBMIT_REGISTER).click()

    def wait_success_redirect_to_login(self):
        self.wait.until(EC.any_of(
            EC.url_contains("/login"),
            EC.visibility_of_element_located(L.HEADER_LOGIN)
        ))
        return True

    def get_password_error_text(self):
        try:
            err = self.wait.until(EC.visibility_of_element_located(R.PASSWORD_ERROR))
            return err.text.strip()
        except Exception:
            return ""
