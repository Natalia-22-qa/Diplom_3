import pytest
from selenium import webdriver
from data import *
from locators.base_page_locators import Login
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(params=["chrome", "firefox"])
def driver(request):
    if request.param == "chrome":
        driver = webdriver.Chrome()
        driver.set_window_size(1920, 1080)
        driver.get(Urls.main_page_site)
    elif request.param == "firefox":
        driver = webdriver.Firefox()
        driver.set_window_size(1920, 1080)
        driver.get(Urls.main_page_site)
    yield driver
    driver.quit()

@pytest.fixture()
def login(driver):
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Login.login_account_button)))
    driver.find_element(*Login.login_account_button).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Login.email_input)))
    driver.find_element(*Login.email_input).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Login.email_field)))
    driver.find_element(*Login.email_field).send_keys(Data.test_email)
    driver.find_element(*Login.password_input).click()
    WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((Login.password_field)))
    driver.find_element(*Login.password_field).send_keys(Data.test_password)
    driver.find_element(*Login.login_button).click()
    yield
