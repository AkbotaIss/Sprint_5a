import pytest
from pages.logout_page import LogoutPage

EMAIL = "Issina_Akbota_31_567@ya.ru"
PASSWORD = "qwerty6"

@pytest.mark.logout
def test_logout_from_profile(chrome, base_url):
    driver = chrome
    try:
        page = LogoutPage(driver, base_url)
        page.login_and_open_profile(EMAIL, PASSWORD)
        assert page.click_logout() is True
    finally:
        driver.quit()
