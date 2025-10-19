
from selenium.webdriver.common.by import By



class CommonLocators:
    CONSTRUCTOR_BTN = (By.XPATH, "//p[normalize-space()='Конструктор']")
    CABINET_BTN = (By.XPATH, "//p[normalize-space()='Личный Кабинет']")
    LOGO_LINK = (By.XPATH, "//a[contains(@class, 'AppHeader_header__logo')]")  # логотип — ссылка на главную



class MainPageLocators:
    MAIN_LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти в аккаунт']")
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[normalize-space()='Оформить заказ']")



class LoginPageLocators:
    HEADER_LOGIN = (By.XPATH, "//h2[normalize-space()='Вход']")
    EMAIL_INPUT = (By.XPATH, "//label[normalize-space()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[normalize-space()='Пароль']/following-sibling::input")
    SUBMIT_LOGIN = (By.XPATH, "//button[normalize-space()='Войти']")
    LINK_TO_REGISTER = (By.XPATH, "//a[normalize-space()='Зарегистрироваться']")



class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, "//label[normalize-space()='Имя']/following-sibling::input")
    EMAIL_INPUT = (By.XPATH, "//label[normalize-space()='Email']/following-sibling::input")
    PASSWORD_INPUT = (By.XPATH, "//label[normalize-space()='Пароль']/following-sibling::input")
    SUBMIT_REGISTER = (By.XPATH, "//button[normalize-space()='Зарегистрироваться']")
    LINK_LOGIN_FROM_REGISTER = (By.XPATH, "//a[normalize-space()='Войти']")
    PASSWORD_ERROR = (By.XPATH, "//*[contains(normalize-space(.), 'Некорректный пароль')]")



class ForgotPasswordLocators:
    EMAIL_INPUT = (By.XPATH, "//label[normalize-space()='Email']/following-sibling::input")
    RESTORE_BUTTON = (By.XPATH, "//button[normalize-space()='Восстановить']")
    LOGIN_BUTTON = (By.XPATH, "//button[normalize-space()='Войти']")



class ProfilePageLocators:
    PROFILE_URL_PART = "/account/profile"
    LOGOUT_BUTTON = (By.XPATH, "//button[normalize-space()='Выход']")



class IngredientsLocators:
    TAB_BUNS = (By.XPATH, "//span[normalize-space()='Булки']/ancestor::*[@role='tab']")
    TAB_SAUCES = (By.XPATH, "//span[normalize-space()='Соусы']/ancestor::*[@role='tab']")
    TAB_FILLINGS = (By.XPATH, "//span[normalize-space()='Начинки']/ancestor::*[@role='tab']")

    SECTION_BUNS = (By.XPATH, "//h2[normalize-space()='Булки']")
    SECTION_SAUCES = (By.XPATH, "//h2[normalize-space()='Соусы']")
    SECTION_FILLINGS = (By.XPATH, "//h2[normalize-space()='Начинки']")
