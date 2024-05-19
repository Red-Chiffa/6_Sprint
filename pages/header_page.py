from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure
from locators.header_locators import HeaderLocators


class HeaderPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('клик по логотипу Яндекс в хедере')
    def ya_logo_click(self):
        self.driver.find_element(*HeaderLocators.ya_logo).click()

    @allure.step('клик по логотипу Самокат в хедере')
    def scooter_logo_click(self):
        self.driver.find_element(*HeaderLocators.scooter_logo).click()

    @allure.step('клик по кнопке Заказать в хедере')
    def order_header_btn_click(self):
        self.driver.find_element(*HeaderLocators.order_header_btn).click()

    @allure.step('клик по кнопке Статус заказа в хедере')
    def order_status_btn_click(self):
        self.driver.find_element(*HeaderLocators.order_status_btn).click()

    @allure.step('получение URL при редиректе')
    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('ожидание URL')
    def wait_for_url(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))

    @allure.step('получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url
