# tests/test_profile.py
import pytest
from pages.profile_page import ProfilePage

EMAIL = "Issina_Akbota_31_567@ya.ru"
PASSWORD = "qwerty6"


@pytest.mark.profile
class TestProfile:
    def test_open_profile_from_main(self, chrome, base_url):
        """Проверка перехода в профиль после авторизации"""
        page = ProfilePage(chrome, base_url)
        page.open_main()
        page.click_cabinet_and_login(EMAIL, PASSWORD)
        assert page.open_profile() is True
