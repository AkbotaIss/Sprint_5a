# pages/ingredients_page.py
from pages.base_page import BasePage
from pages.locators import IngredientsLocators as I


class IngredientsPage(BasePage):
    PATH_MAIN = "/"

    def __init__(self, driver, base_url):
        super().__init__(driver, base_url)

    def open(self):
        """Открыть главную страницу и дождаться загрузки секции Булки"""
        self.open(self.PATH_MAIN)
        self.wait_visible(I.SECTION_BUNS)

    def click_buns(self):
        """Клик по вкладке 'Булки'"""
        self.click(I.TAB_BUNS)
        return self._is_active(I.TAB_BUNS)

    def click_sauces(self):
        """Клик по вкладке 'Соусы'"""
        self.click(I.TAB_SAUCES)
        return self._is_active(I.TAB_SAUCES)

    def click_fillings(self):
        """Клик по вкладке 'Начинки'"""
        self.click(I.TAB_FILLINGS)
        return self._is_active(I.TAB_FILLINGS)

    def _is_active(self, tab_locator):
        """Проверка, что вкладка активна"""
        el = self.wait_visible(tab_locator)
        aria = el.get_attribute("aria-selected") or ""
        cls = el.get_attribute("class") or ""
        return aria.lower() == "true" or "current" in cls or "active" in cls
