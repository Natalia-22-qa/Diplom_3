from selenium.webdriver.common.by import By


class MainPageLocators:
    # надпись "Соберите бургер" на странице конструктора
    constructor_title = (By.XPATH, ".//h1[text() = 'Соберите бургер']")
    # заголовок всплывающего окна "Детали ингредиента"
    ingredient_details_title = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title') and text() = 'Детали ингредиента']")
    # всплывающее окно "Детали ингредиента"
    ingredient_details = (By.XPATH, ".//div[contains(@class, 'Modal_modal__container')]")
    # кнопка закрытия окна деталей ингредиента в виде крестика
    close_details_button = (By.XPATH, ".//section[contains(@class, 'Modal_modal_opened')]//button[contains(@class, 'Modal_modal__close')]")
    # зона сбора заказа (бургера)
    #constructor_space = (By.XPATH, ".//section[contains(@class, 'BurgerConstructor_basket')]")
    constructor_space = (By.XPATH, ".//ul[contains(@class, 'BurgerConstructor_basket__list__')]")
    # ингредиент (булочка)
    ingredients = (By.XPATH, ".//ul[1]/a[1]")
    # счетчик ингредиента (булочки)
    ingredient_counter = (By.XPATH, ".//ul[1]/a[1]//p[contains(@class, 'counter_counter__num')]")
    # кнопка "Оформить заказ"
    create_order_button = (By.XPATH, ".//button[text() = 'Оформить заказ']")
    # номер оформленного заказа
    order_number = (By.XPATH, ".//h2[contains(@class, 'Modal_modal__title_shadow')]")
    # кнопка закрытия окна с номером заказа
    close_order_number_button = (By.XPATH, ".//button[contains(@class, 'Modal_modal__close_modified')]")
