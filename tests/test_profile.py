import pytest
from pages.profile_page import ProfilePage

EMAIL = "Issina_Akbota_31_567@ya.ru"
PASSWORD = "qwerty6"

@pytest.mark.profile
def test_open_profile_from_main(chrome, base_url):
    driver = chrome
    try:
        page = ProfilePage(driver, base_url)
        page.open_main()
        page.click_cabinet_and_login(EMAIL, PASSWORD)
        assert page.open_profile() is True
    finally:
        driver.quit()
