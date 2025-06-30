from selenium.webdriver.common.by import By


class OrderPageLocators:
    # надпись "Лента заказов" на странице заказов
    order_feed_title = (By.XPATH, ".//h1[text() = 'Лента заказов']")
    # строка с количеством заказов за всё время
    all_order_quantity = (By.XPATH, ".//p[text()='Выполнено за все время:']/following-sibling::p")
    # строка с количеством заказов за сегодня
    today_order_quantity = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/following-sibling::p")
    # лист с номерами заказов "В работе"
    order_list = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady')]/li")
