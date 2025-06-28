from selenium.webdriver.common.by import By


class BasePageLocators:
    # элемент прогрузки страницы
    overlay = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")  # прозрачный элемент
    # кнопка "Конструктор" в шапке
    constructor_button = (By.XPATH, ".//li[1]")
    # кнопка "Лента Заказов" в шапке
    order_feed_button = (By.XPATH, ".//li[2]")

class Login:
    # кнопка "Войти в аккаунт" на главной странице
    login_account_button = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")
    # поле "Email"
    email_input = (By.XPATH, ".//fieldset[1]//label[text() = 'Email']")
    # поле для ввода логина (Email)
    email_field = (By.XPATH, ".//fieldset[1]//input[@value = '']")
    # поле "Пароль"
    password_input = (By.XPATH, ".//fieldset[2]//label[text() = 'Пароль']")
    # поле для ввода пароля
    password_field = (By.XPATH, ".//fieldset[2]//input[@value = '']")
    # кнопка "Войти"
    login_button = (By.XPATH, ".//button[text() = 'Войти']")

