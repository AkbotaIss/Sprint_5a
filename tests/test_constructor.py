
import pytest
from pages.constructor_page import ConstructorPage


EMAIL = "Issina_Akbota_31_567@ya.ru"
PASSWORD = "qwerty6"


@pytest.mark.constructor
class TestConstructor:
    @pytest.mark.smoke
    def test_click_constructor_returns_to_main(self, chrome, base_url):
        """
        Авторизация → переход в профиль → клик по 'Конструктор' → возврат на главную страницу.
        """
        page = ConstructorPage(chrome, base_url)
        page.login_and_open_profile(EMAIL, PASSWORD)
        result = page.click_constructor()
        assert result is True, "После клика на 'Конструктор' не открылся главный экран"

    @pytest.mark.smoke
    def test_click_logo_returns_to_main(self, chrome, base_url):
        """
        Авторизация → переход в профиль → клик по логотипу → возврат на главную страницу.
        """
        page = ConstructorPage(chrome, base_url)
        page.login_and_open_profile(EMAIL, PASSWORD)
        result = page.click_logo()
        assert result is True, "После клика на логотип не открылся главный экран"
