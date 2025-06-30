import allure
from conftest import *
from data import Data
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestMainFunctions:

    @allure.title('Проверка перехода в раздел "Лента заказов" по клику на одноименную кнопку')
    def test_cross_to_order_feed_page_success(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.wait_when_overlay_hide()
        main_page.wait_visibility_of_order_feed_button()
        main_page.click_on_order_feed_button()
        order_page.wait_visibility_of_order_feed_title()
        assert order_page.get_text_on_order_feed_title() == Data.text_order_feed_title

    @allure.title('Проверка перехода в раздел "Конструктор" по клику на одноименную кнопку')
    def test_cross_to_constructor_page_success(self, driver):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.wait_when_overlay_hide()
        main_page.wait_visibility_of_order_feed_button()
        main_page.click_on_order_feed_button()
        order_page.wait_visibility_of_order_feed_title()
        main_page.click_on_constructor_button()
        main_page.wait_visibility_of_constructor_title()
        assert main_page.get_text_on_constructor_title() == Data.text_constructor_title

    @allure.title('Проверка появления всплывающего окна "Детали ингредиента" по клику на ингредиент')
    def test_open_ingredient_details_success(self, driver):
        main_page = MainPage(driver)
        main_page.wait_when_overlay_hide()
        main_page.wait_visibility_of_ingredients()
        main_page.click_on_ingredients()
        main_page.wait_visibility_of_ingredient_details_title()
        assert main_page.check_displaying_of_ingredient_details()

    @allure.title('Проверка закрытия всплывающего окна "Детали ингредиента" по клику на ингредиент')
    def test_close_ingredient_details_success(self, driver):
        main_page = MainPage(driver)
        main_page.wait_when_overlay_hide()
        main_page.wait_visibility_of_ingredients()
        main_page.click_on_ingredients()
        main_page.wait_visibility_of_ingredient_details_title()
        main_page.click_on_close_details_button()
        main_page.wait_closing_of_ingredient_details()
        assert main_page.check_displaying_of_ingredient_details() is not True

    @allure.title('Проверка увеличения счетчика ингредиента при добавлении этого ингредиента в заказ')
    def test_increase_of_count_ingredient_in_order_success(self, driver):
        main_page = MainPage(driver)
        main_page.wait_when_overlay_hide()
        main_page.wait_visibility_of_ingredients()
        main_page.drag_and_drop_ingredients()
        assert main_page.get_text_on_ingredient_counter() != '0'

# pytest tests/test_main_functions.py
