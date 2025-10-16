from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.locators import IngredientsLocators as I

class IngredientsPage:
    PATH_MAIN = "/"

    def __init__(self, driver, base_url):
        self.driver = driver
        self.base_url = base_url
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get(self.base_url + self.PATH_MAIN)
        self.wait.until(EC.visibility_of_element_located(I.SECTION_BUNS))

    def click_buns(self):
        self.wait.until(EC.element_to_be_clickable(I.TAB_BUNS)).click()
        return self._is_active(I.TAB_BUNS)

    def click_sauces(self):
        self.wait.until(EC.element_to_be_clickable(I.TAB_SAUCES)).click()
        return self._is_active(I.TAB_SAUCES)

    def click_fillings(self):
        self.wait.until(EC.element_to_be_clickable(I.TAB_FILLINGS)).click()
        return self._is_active(I.TAB_FILLINGS)

    def _is_active(self, tab_locator):
        el = self.wait.until(EC.visibility_of_element_located(tab_locator))
        aria = el.get_attribute("aria-selected") or ""
        cls = el.get_attribute("class") or ""
        return aria.lower() == "true" or "current" in cls or "active" in cls
