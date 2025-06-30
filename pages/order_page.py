import allure
from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage
from data import Data


class OrderPage(BasePage):

    @allure.step('Подождать прогрузки отображения заголовка страницы заказов')
    def wait_visibility_of_order_feed_title(self):
        self.wait_visibility_of_element(OrderPageLocators.order_feed_title)

    @allure.step('Получить текст заголовка "Лента Заказов"')
    def get_text_on_order_feed_title(self):
        return self.get_text_on_element(OrderPageLocators.order_feed_title)

    @allure.step('Получить текст строки с количеством заказов за всё время')
    def get_text_on_all_order_quantity(self):
        return self.get_text_on_element(OrderPageLocators.all_order_quantity)

    @allure.step('Получить текст строки с количеством заказов за сегодня')
    def get_text_on_today_order_quantity(self):
        return self.get_text_on_element(OrderPageLocators.today_order_quantity)

    @allure.step('Получить текст листа с номерами заказов "В работе"')
    def get_text_on_order_list(self):
        return self.get_text_on_element(OrderPageLocators.order_list)

    @allure.step('Подождать изменения значения в разделе "В работе"')
    def wait_changing_of_order_list(self):
        return self.wait_changing_of_element_count(OrderPageLocators.order_list, Data.text_order_list_completed)
