import allure
from locators.login_page_locators import Login
from pages.base_page import BasePage
from data import Data


class LoginPage(BasePage):

    @allure.step('Подождать прогрузки кнопки "Войти в аккаунт"')
    def wait_visibility_of_login_account_button(self):
        self.wait_visibility_of_element(Login.login_account_button)

    @allure.step('Кликнуть на кнопку "Войти в аккаунт"')
    def click_on_login_account_button(self):
        self.click_on_element(Login.login_account_button)

    @allure.step('Подождать появления поля "Email"')
    def wait_visibility_of_email_input(self):
        self.wait_visibility_of_element(Login.email_input)

    @allure.step('Кликнуть на поле "Email"')
    def click_on_email_input(self):
        self.click_on_element(Login.email_input)

    @allure.step('Подождать появления поля ввода логина')
    def wait_visibility_of_email_field(self):
        self.wait_visibility_of_element(Login.email_field)

    @allure.step('Ввести значение в поле ввода логина')
    def send_keys_to_email_field(self):
        self.send_keys_to_input(Login.email_field, Data.test_email)

    @allure.step('Кликнуть на поле "Пароль"')
    def click_on_password_input(self):
        self.click_on_element(Login.password_input)

    @allure.step('Подождать появления поля ввода пароля')
    def wait_visibility_of_password_field(self):
        self.wait_visibility_of_element(Login.password_field)

    @allure.step('Ввести значение в поле ввода пароля')
    def send_keys_to_password_field(self):
        self.send_keys_to_input(Login.password_field, Data.test_password)

    @allure.step('Кликнуть на кнопку "Войти"')
    def click_on_login_button(self):
        self.click_on_element(Login.login_button)
