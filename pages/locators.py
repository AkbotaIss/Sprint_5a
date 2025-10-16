from selenium.webdriver.common.by import By

# Общие элементы, встречающиеся на разных страницах
class CommonLocators:
    CONSTRUCTOR_BTN = (By.XPATH, "//p[text()='Конструктор']")             # Кнопка «Конструктор» в шапке
    CABINET_BTN = (By.XPATH, "//p[text()='Личный Кабинет']")              # Кнопка «Личный кабинет» в шапке
    LOGO_LINK = (By.XPATH, "//div[contains(@class,'AppHeader_header__logo')]//a")  # Логотип Stellar Burgers (ссылка на главную)

# Главная страница
class MainPageLocators:
    MAIN_LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")  # Кнопка «Войти в аккаунт» на главной
    MAKE_ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")   # Кнопка «Оформить заказ» (появляется после входа)

# Страница входа
class LoginPageLocators:
    HEADER_LOGIN = (By.XPATH, "//h2[text()='Вход']")                      # Заголовок страницы «Вход»
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")    # Поле Email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")# Поле Пароль
    SUBMIT_LOGIN = (By.XPATH, "//button[text()='Войти']")                 # Кнопка «Войти»

# Страница регистрации
class RegistrationPageLocators:
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")       # Поле Имя
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")    # Поле Email
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")# Поле Пароль
    SUBMIT_REGISTER = (By.XPATH, "//button[text()='Зарегистрироваться']")           # Кнопка «Зарегистрироваться»
    LINK_LOGIN_FROM_REGISTER = (By.XPATH, "//a[text()='Войти']")                    # Ссылка «Войти» со страницы регистрации
    PASSWORD_ERROR = (By.XPATH, "//p[contains(text(),'Некорректный пароль')]")      # Ошибка «Некорректный пароль»

# Страница «Забыли пароль»
class ForgotPasswordLocators:
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")                 # Кнопка «Войти» на форме восстановления

# Личный кабинет / профиль
class ProfilePageLocators:
    PROFILE_URL_PART = "/account/profile"                                 # Часть URL профиля для проверки перехода
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")                # Кнопка «Выход» в личном кабинете

# Конструктор — вкладки ингредиентов
class IngredientsLocators:
    TAB_BUNS = (By.XPATH, "(//span[text()='Булки']/ancestor::*[@role='tab' or contains(@class,'tab')])[1]")       # Вкладка «Булки»
    TAB_SAUCES = (By.XPATH, "(//span[text()='Соусы']/ancestor::*[@role='tab' or contains(@class,'tab')])[1]")     # Вкладка «Соусы»
    TAB_FILLINGS = (By.XPATH, "(//span[text()='Начинки']/ancestor::*[@role='tab' or contains(@class,'tab')])[1]") # Вкладка «Начинки»

    SECTION_BUNS = (By.XPATH, "//h2[text()='Булки']")                      # Заголовок секции «Булки»
    SECTION_SAUCES = (By.XPATH, "//h2[text()='Соусы']")                    # Заголовок секции «Соусы»
    SECTION_FILLINGS = (By.XPATH, "//h2[text()='Начинки']")                # Заголовок секции «Начинки»
