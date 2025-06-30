from selenium.webdriver.common.by import By


class BasePageLocators:
    # элемент прогрузки страницы
    overlay = (By.XPATH, ".//div[contains(@class, 'Modal_modal_overlay__x2ZCr')]/parent::div")  # прозрачный элемент
    # кнопка "Конструктор" в шапке
    constructor_button = (By.XPATH, ".//p[text() = 'Конструктор']")
    # кнопка "Лента Заказов" в шапке
    order_feed_button = (By.XPATH, ".//p[text() = 'Лента Заказов']")
