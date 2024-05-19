import pytest
from selenium import webdriver
from config import BASE_URL
from locators.main_page_locators import MainPageLocators


@pytest.fixture
def driver():
    firefox = webdriver.Firefox()
    firefox.get(BASE_URL)
    firefox.maximize_window()
    firefox.find_element(*MainPageLocators.close_cookie_btn).click()
    yield firefox
    firefox.quit()
