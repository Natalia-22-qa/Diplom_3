import allure
from conftest import *
from pages.main_page import MainPage
from pages.order_page import OrderPage


class TestOrderFeed:

    @allure.title('Проверка увеличения счетчика "Выполнено за всё время" при создании нового заказа')
    def test_increase_of_count_orders_for_all_time_success(self, driver, login):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.wait_when_overlay_hide()
        main_page.wait_visibility_of_order_feed_button()
        main_page.click_on_order_feed_button()
        order_page.wait_visibility_of_order_feed_title()
        count_1 = order_page.get_text_on_all_order_quantity()
        main_page.click_on_constructor_button()
        main_page.wait_visibility_of_ingredients()
        main_page.drag_and_drop_ingredients()
        main_page.click_on_create_order_button()
        main_page.wait_visibility_of_order_number()
        main_page.wait_when_overlay_hide()
        main_page.click_on_close_close_order_number_button()
        main_page.click_on_order_feed_button()
        order_page.wait_visibility_of_order_feed_title()
        count_2 = order_page.get_text_on_all_order_quantity()
        assert int(count_2) - int(count_1) > 0

    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" при создании нового заказа')
    def test_increase_of_count_orders_today_success(self, driver, login):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.wait_when_overlay_hide()
        main_page.wait_visibility_of_order_feed_button()
        main_page.click_on_order_feed_button()
        order_page.wait_visibility_of_order_feed_title()
        count_1 = order_page.get_text_on_today_order_quantity()
        main_page.click_on_constructor_button()
        main_page.wait_visibility_of_ingredients()
        main_page.drag_and_drop_ingredients()
        main_page.click_on_create_order_button()
        main_page.wait_visibility_of_order_number()
        main_page.wait_when_overlay_hide()
        main_page.click_on_close_close_order_number_button()
        main_page.click_on_order_feed_button()
        order_page.wait_visibility_of_order_feed_title()
        count_2 = order_page.get_text_on_today_order_quantity()
        assert int(count_2) - int(count_1) > 0

    @allure.title('Проверка появления номера оформленного заказа в разделе "В работе"')
    def test_check_new_order_number_in_order_list_true(self, driver, login):
        main_page = MainPage(driver)
        order_page = OrderPage(driver)
        main_page.wait_when_overlay_hide()
        main_page.wait_visibility_of_ingredients()
        main_page.drag_and_drop_ingredients()
        main_page.click_on_create_order_button()
        main_page.wait_visibility_of_order_number()
        main_page.wait_when_overlay_hide()
        number = main_page.get_text_on_order_number()
        main_page.click_on_close_close_order_number_button()
        main_page.click_on_order_feed_button()
        order_page.wait_visibility_of_order_feed_title()
        order_page.wait_changing_of_order_list()
        assert number in order_page.get_text_on_order_list()

# pytest tests/test_order_feed.py
