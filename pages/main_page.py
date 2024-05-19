from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
import allure


class MainPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('клик по кнопке принятия куки')
    def close_cookie(self):
        self.driver.find_element(*MainPageLocators.close_cookie_btn).click()

    @allure.step('клик по вопросу')
    def question_click(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('получение текста ответа')
    def get_answer_text(self, locator):
        return self.driver.find_element(*locator).text

    @allure.step('ожидвание отображения элемента')
    def timeout(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
