import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('клик по элементу')
    def click_element(self, element):
        self.driver.find_element(*element).click()

    #    @allure.step('получение URL при редиректе')
    @allure.step('переключение на другую страницу по редиректу')
    def switch_to_window(self):
        self.driver.switch_to.window(self.driver.window_handles[1])

    @allure.step('ожидание URL')
    def timeout_url(self, url):
        WebDriverWait(self.driver, 5).until(expected_conditions.url_to_be(url))

    @allure.step('ожидание отображения элемента')
    def timeout(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('получение текущего URL')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('заполнение инпутк')
    def fill_input(self, locator, text):
        self.driver.find_element(*locator).send_keys(text)

    @allure.step('получение текста элемента')
    def get_element_text(self, locator):
        return self.driver.find_element(*locator).text


