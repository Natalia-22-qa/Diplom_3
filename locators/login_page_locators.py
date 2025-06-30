from selenium.webdriver.common.by import By


class Login:
    # кнопка "Войти в аккаунт" на главной странице
    login_account_button = (By.XPATH, ".//button[text() = 'Войти в аккаунт']")
    # поле "Email"
    email_input = (By.XPATH, ".//label[text() = 'Email']")
    # поле для ввода логина (Email)
    email_field = (By.XPATH, ".//label[text() = 'Email']/following-sibling::input")
    # поле "Пароль"
    password_input = (By.XPATH, ".//label[text() = 'Пароль']")
    # поле для ввода пароля
    password_field = (By.XPATH, ".//label[text() = 'Пароль']/following-sibling::input")
    # кнопка "Войти"
    login_button = (By.XPATH, ".//button[text() = 'Войти']")
