import pytest
from selenium import webdriver
from urls import Urls
from pages.login_page import LoginPage


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
    login_page = LoginPage(driver)
    login_page.wait_visibility_of_login_account_button()
    login_page.click_on_login_account_button()
    login_page.wait_visibility_of_email_input()
    login_page.click_on_email_input()
    login_page.wait_visibility_of_email_field()
    login_page.send_keys_to_email_field()
    login_page.click_on_password_input()
    login_page.wait_visibility_of_password_field()
    login_page.send_keys_to_password_field()
    login_page.click_on_login_button()
