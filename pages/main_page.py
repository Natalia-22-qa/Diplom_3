import allure
from locators.main_page_locators import MainPageLocators
from locators.base_page_locators import BasePageLocators
from pages.base_page import BasePage


class MainPage(BasePage):

    @allure.step('Подождать когда пропадет элемент прогрузки страницы')
    def wait_when_overlay_hide(self):
        self.wait_closing_of_element(BasePageLocators.overlay)

    @allure.step('Кликнуть на кнопку "Конструктор" в шапке')
    def click_on_constructor_button(self):
        self.click_on_element(BasePageLocators.constructor_button)

    @allure.step('Подождать прогрузки кнопки "Лента Заказов" в шапке')
    def wait_visibility_of_order_feed_button(self):
        self.wait_visibility_of_element(BasePageLocators.order_feed_button)

    @allure.step('Кликнуть на кнопку "Лента Заказов" в шапке')
    def click_on_order_feed_button(self):
        self.click_on_element(BasePageLocators.order_feed_button)

    @allure.step('Подождать отображения заголовка конструктора')
    def wait_visibility_of_constructor_title(self):
        self.wait_visibility_of_element(MainPageLocators.constructor_title)

    @allure.step('Подождать отображения ингредиента')
    def wait_visibility_of_ingredients(self):
        self.wait_visibility_of_element(MainPageLocators.ingredients)

    @allure.step('Кликнуть на ингредиент')
    def click_on_ingredients(self):
        self.click_on_element(MainPageLocators.ingredients)

    @allure.step('Подождать отображения заголовка всплывающего окна "Детали ингредиента"')
    def wait_visibility_of_ingredient_details_title(self):
        self.wait_visibility_of_element(MainPageLocators.ingredient_details_title)

    @allure.step('Проверить отображение всплывающего окна "Детали ингредиента"')
    def check_displaying_of_ingredient_details(self):
        return self.check_displaying_of_element(MainPageLocators.ingredient_details)

    @allure.step('Кликнуть на кнопку-крестик, чтобы закрыть окно "Детали ингредиента"')
    def click_on_close_details_button(self):
        self.click_on_element(MainPageLocators.close_details_button)

    @allure.step('Перетащить ингредиент в зону сбора бургера')
    def drag_and_drop_ingredients(self):
        source = self.find_element(MainPageLocators.ingredients)
        target = self.find_element(MainPageLocators.constructor_space)
        self.drag_and_drop_element(source, target)

    @allure.step('Получить число ингредиента в бургере')
    def get_text_on_ingredient_counter(self):
        return self.get_text_on_element(MainPageLocators.ingredient_counter)

    @allure.step('Получить текст заголовка "Конструктор"')
    def get_text_on_constructor_title(self):
        return self.get_text_on_element(MainPageLocators.constructor_title)

    @allure.step('Подождать закрытия окна "Детали ингредиента"')
    def wait_closing_of_ingredient_details(self):
        self.wait_closing_of_element(MainPageLocators.ingredient_details)

    @allure.step('Кликнуть на кнопку "Оформить заказ"')
    def click_on_create_order_button(self):
        self.click_on_element(MainPageLocators.create_order_button)

    @allure.step('Подождать отображения номера оформленного заказа')
    def wait_visibility_of_order_number(self):
        self.wait_visibility_of_element(MainPageLocators.order_number)

    @allure.step('Получить номер оформленного заказа')
    def get_text_on_order_number(self):
        return self.get_text_on_element(MainPageLocators.order_number)

    @allure.step('Кликнуть на кнопку-крестик, чтобы закрыть окно с номером заказа')
    def click_on_close_close_order_number_button(self):
        self.click_on_element(MainPageLocators.close_order_number_button)
