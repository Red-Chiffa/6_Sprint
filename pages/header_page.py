import allure
from locators.header_locators import HeaderLocators
from pages.base_page import BasePage


class HeaderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('клик по логотипу Яндекс в хедере')
    def ya_logo_click(self):
        self.click_element((HeaderLocators.ya_logo))

    @allure.step('клик по логотипу Самокат в хедере')
    def scooter_logo_click(self):
        self.click_element((HeaderLocators.scooter_logo))

    @allure.step('клик по кнопке Заказать в хедере')
    def order_header_btn_click(self):
        self.click_element((HeaderLocators.order_header_btn))

    @allure.step('клик по кнопке Статус заказа в хедере')
    def order_status_btn_click(self):
        self.click_element((HeaderLocators.order_status_btn))

    @allure.step('клик по кнопке принятия куки')
    def close_cookie(self):
        self.click_element((HeaderLocators.close_cookie_btn))
