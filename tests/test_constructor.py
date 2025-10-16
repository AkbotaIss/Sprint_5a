import pytest
from pages.constructor_page import ConstructorPage

EMAIL = "Issina_Akbota_31_567@ya.ru"
PASSWORD = "qwerty6"

@pytest.mark.constructor
def test_transition_from_profile_to_constructor_button(chrome, base_url):
    driver = chrome
    try:
        page = ConstructorPage(driver, base_url)
        page.login_and_open_profile(EMAIL, PASSWORD)
        assert page.click_constructor() is True
    finally:
        driver.quit()

@pytest.mark.constructor
def test_transition_from_profile_to_constructor_logo(chrome, base_url):
    driver = chrome
    try:
        page = ConstructorPage(driver, base_url)
        page.login_and_open_profile(EMAIL, PASSWORD)
        assert page.click_logo() is True
    finally:
        driver.quit()
