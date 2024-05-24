from locators.main_page_locators import MainPageLocators
import allure

from pages.base_page import BasePage


class MainPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('клик по вопросу')
    def question_click(self, locator):
        self.click_element(locator)

    @allure.step('получение текста ответа')
    def get_answer_text(self, locator):
        return self.get_element_text(locator)

    @allure.step('клик по кнопке принятия куки')
    def close_cookie(self):
        self.click_element((MainPageLocators.close_cookie_btn))
