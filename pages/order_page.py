import allure

from locators.order_page_locators import OrderPageLocators
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class OrderPage:

    def __init__(self, driver):
        self.driver = driver

    @allure.step('клик по кнопке заказать на главной странице')
    def order_btn_main_page_click(self):
        self.driver.find_element(*MainPageLocators.order_btn).click()

    @allure.step('ожидвание отображения элемента')
    def timeout(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('заполнение поля Имя')
    def fill_name(self, name):
        self.driver.find_element(*OrderPageLocators.name_input).send_keys(name)

    @allure.step('заполнение поля Фамилия')
    def fill_surname(self, surname):
        self.driver.find_element(*OrderPageLocators.surname_input).send_keys(surname)

    @allure.step('заполнение поля Адрес')
    def fill_adress(self, adress):
        self.driver.find_element(*OrderPageLocators.adress_input).send_keys(adress)

    @allure.step('выбор станции метро')
    def choose_metro_station(self):
        self.driver.find_element(*OrderPageLocators.metro_input).click()
        self.driver.find_element(*OrderPageLocators.metro_station_choose).click()

    @allure.step('заполнение поля Телефон')
    def fill_phone_number(self, phone_number):
        self.driver.find_element(*OrderPageLocators.phone_number_input).send_keys(phone_number)

    @allure.step('клик по кнопке Далее')
    def go_on_btn_click(self):
        self.driver.find_element(*OrderPageLocators.next_btn).click()

    @allure.step('выбор даты доставки')
    def delivery_date_choose(self):
        self.driver.find_element(*OrderPageLocators.date_input).click()
        self.driver.find_element(*OrderPageLocators.calendar_choose_day).click()

    @allure.step('выбор срока аренды')
    def rental_period_choose(self):
        self.driver.find_element(*OrderPageLocators.rental_period_input).click()
        self.driver.find_element(*OrderPageLocators.rental_period).click()

    @allure.step('клик в чек-боксе черный жемчуг')
    def black_color_choose(self):
        self.driver.find_element(*OrderPageLocators.checkbox_black).click()

    @allure.step('клик в чек-боксе серая безысходность')
    def grey_color_choose(self):
        self.driver.find_element(*OrderPageLocators.checkbox_grey).click()

    @allure.step('заполнение поля Комментарий для курьера')
    def fill_comment(self, comment):
        self.driver.find_element(*OrderPageLocators.comment_input).send_keys(comment)

    @allure.step('клик по кнопке Заказать')
    def create_order_btn_click(self):
        self.driver.find_element(*OrderPageLocators.create_order_btn).click()

    @allure.step('клик по кнопке Да на модальном окне')
    def confirm_orger_btn_click(self):
        self.driver.find_element(*OrderPageLocators.confirm_orger_btn).click()

    @allure.step('клик по кнопке Посмотреть статус на модальном окне')
    def check_status_modal(self):
        self.driver.find_element(*OrderPageLocators.check_status).click()
