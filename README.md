# Sprint_5a — Selenium-тесты для Stellar Burgers

Автоматизированные UI-тесты для учебного сайта [Stellar Burgers](https://stellarburgers.education-services.ru).  
Проект выполнен в рамках задания Sprint 5 (Яндекс.Практикум).

---

## 🚀 Цель проекта
Проверить основные пользовательские сценарии:
- Регистрация и валидация пароля
- Вход различными способами
- Переходы между страницами (личный кабинет, конструктор)
- Выход из аккаунта
- Переключение вкладок конструктора («Булки», «Соусы», «Начинки»)

---

## 🧩 Структура проекта

Sprint_5a/
├── pages/ # Page Object классы
│ ├── constructor_page.py
│ ├── ingredients_page.py
│ ├── locators.py
│ ├── login_page.py
│ ├── logout_page.py
│ ├── profile_page.py
│ └── registration_page.py
│
├── tests/ # Автотесты по модулям
│ ├── test_constructor.py
│ ├── test_ingredients_tabs.py
│ ├── test_login.py
│ ├── test_logout.py
│ ├── test_profile.py
│ └── test_registration.py
│
├── utils/ # Генераторы данных
│ └── generators.py
│
├── conftest.py # Общие фикстуры
├── requirements.txt # Зависимости проекта
├── .gitignore
└── README.md