import allure
from locators.order_page_locators import OrderPageLocators


from pages.base_page import BasePage


class OrderPage(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    @allure.step('клик по кнопке заказать на главной странице')
    def order_btn_main_page_click(self):
        self.click_element((OrderPageLocators.order_btn))

    @allure.step('заполнение поля Имя')
    def fill_name(self, name):
        self.fill_input((OrderPageLocators.name_input), name)

    @allure.step('заполнение поля Фамилия')
    def fill_surname(self, surname):
        self.fill_input((OrderPageLocators.surname_input), surname)

    @allure.step('заполнение поля Адрес')
    def fill_adress(self, adress):
        self.fill_input((OrderPageLocators.adress_input), adress)

    @allure.step('выбор станции метро')
    def choose_metro_station(self):
        self.click_element((OrderPageLocators.metro_input))
        self.click_element((OrderPageLocators.metro_station_choose))

    @allure.step('заполнение поля Телефон')
    def fill_phone_number(self, phone_number):
        self.fill_input((OrderPageLocators.phone_number_input), phone_number)

    @allure.step('клик по кнопке Далее')
    def go_on_btn_click(self):
        self.click_element((OrderPageLocators.next_btn))

    @allure.step('выбор даты доставки')
    def delivery_date_choose(self):
        self.click_element((OrderPageLocators.date_input))
        self.click_element((OrderPageLocators.calendar_choose_day))

    @allure.step('выбор срока аренды')
    def rental_period_choose(self):
        self.click_element((OrderPageLocators.rental_period_input))
        self.click_element((OrderPageLocators.rental_period))

    @allure.step('клик в чек-боксе черный жемчуг')
    def black_color_choose(self):
        self.click_element((OrderPageLocators.checkbox_black))

    @allure.step('клик в чек-боксе серая безысходность')
    def grey_color_choose(self):
        self.click_element((OrderPageLocators.checkbox_grey))

    @allure.step('заполнение поля Комментарий для курьера')
    def fill_comment(self, comment):
        self.fill_input((OrderPageLocators.comment_input), comment)

    @allure.step('клик по кнопке Заказать')
    def create_order_btn_click(self):
        self.click_element((OrderPageLocators.create_order_btn))

    @allure.step('клик по кнопке Да на модальном окне')
    def confirm_orger_btn_click(self):
        self.click_element((OrderPageLocators.confirm_orger_btn))

    @allure.step('клик по кнопке Посмотреть статус на модальном окне')
    def check_status_modal(self):
        self.click_element((OrderPageLocators.check_status))

    def check_check_status_btn_is_displayed(self):
        return self.check_element_is_displayed(OrderPageLocators.check_status)

    def timeout_name_input(self):
        self.timeout((OrderPageLocators.name_input))
    def timeout_date_delivery(self):
        self.timeout((OrderPageLocators.date_input))
