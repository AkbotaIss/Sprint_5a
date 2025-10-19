# tests/test_logout.py
import pytest
from pages.logout_page import LogoutPage

EMAIL = "Issina_Akbota_31_567@ya.ru"
PASSWORD = "qwerty6"


@pytest.mark.logout
class TestLogout:
    def test_logout_from_profile(self, chrome, base_url):
        """Проверка выхода из профиля"""
        page = LogoutPage(chrome, base_url)
        page.login_and_open_profile(EMAIL, PASSWORD)
        assert page.click_logout() is True, "После выхода не произошло редиректа"
