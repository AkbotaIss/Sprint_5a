# tests/test_ingredients_tabs.py
import pytest
from pages.ingredients_page import IngredientsPage


@pytest.mark.constructor_tabs
class TestIngredientsTabs:
    def test_tabs_buns(self, chrome, base_url):
        """Проверка открытия вкладки 'Булки'"""
        page = IngredientsPage(chrome, base_url)
        page.open()
        assert page.click_buns() is True

    def test_tabs_sauces(self, chrome, base_url):
        """Проверка открытия вкладки 'Соусы'"""
        page = IngredientsPage(chrome, base_url)
        page.open()
        assert page.click_sauces() is True

    def test_tabs_fillings(self, chrome, base_url):
        """Проверка открытия вкладки 'Начинки'"""
        page = IngredientsPage(chrome, base_url)
        page.open()
        assert page.click_fillings() is True
