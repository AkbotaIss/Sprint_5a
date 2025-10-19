# pages/base_page.py
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver, base_url, timeout: int = 10):
        self.driver = driver
        self.base_url = base_url
        self.timeout = timeout

    # -------- Навигация --------
    def open(self, path: str = ""):
        self.driver.get(self.base_url + path)

    def current_url(self) -> str:
        return self.driver.current_url

    # -------- Ожидания URL --------
    def wait_url_contains(self, fragment: str, timeout: int | None = None):
        WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.url_contains(fragment)
        )

    def wait_url_to_be(self, url: str, timeout: int | None = None):
        WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.url_to_be(url)
        )

    # -------- Элементы --------
    def wait_visible(self, locator, timeout: int | None = None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.visibility_of_element_located(locator)
        )

    def wait_clickable(self, locator, timeout: int | None = None):
        return WebDriverWait(self.driver, timeout or self.timeout).until(
            EC.element_to_be_clickable(locator)
        )

    def click(self, locator, timeout: int | None = None):
        self.wait_clickable(locator, timeout).click()

    def type(self, locator, text: str, timeout: int | None = None, clear=True):
        el = self.wait_visible(locator, timeout)
        if clear:
            el.clear()
        el.send_keys(text)

    def scroll_into_view(self, locator, block: str = "center", timeout: int | None = None):
        el = self.wait_visible(locator, timeout)
        self.driver.execute_script(f"arguments[0].scrollIntoView({{block: '{block}'}});", el)
        return el
