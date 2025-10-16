import pytest
from pages.ingredients_page import IngredientsPage

@pytest.mark.constructor_tabs
def test_tabs_buns(chrome, base_url):
    driver = chrome
    try:
        page = IngredientsPage(driver, base_url)
        page.open()
        assert page.click_buns() is True
    finally:
        driver.quit()

@pytest.mark.constructor_tabs
def test_tabs_sauces(chrome, base_url):
    driver = chrome
    try:
        page = IngredientsPage(driver, base_url)
        page.open()
        assert page.click_sauces() is True
    finally:
        driver.quit()

@pytest.mark.constructor_tabs
def test_tabs_fillings(chrome, base_url):
    driver = chrome
    try:
        page = IngredientsPage(driver, base_url)
        page.open()
        assert page.click_fillings() is True
    finally:
        driver.quit()
