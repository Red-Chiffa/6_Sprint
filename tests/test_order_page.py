import pytest
from pages.order_page import *
from pages.main_page import *
from config import ORDER_PAGE_URL


class TestOrderPage:

    @allure.title('переход на  страницу оформления заказа с главной страницы')
    def test_go_to_order_page_from_main_page(self, driver):
        order_page = OrderPage(driver)
        order_page.close_cookie()
        order_page.order_btn_main_page_click()
        assert driver.current_url == ORDER_PAGE_URL

    @allure.description('параметризованный тест проверяет хэппи-пасс оформления заказа')
    @allure.title('оформление заказа')
    @pytest.mark.parametrize('name, surname, adress, phone_number, comment',
                             [('Маша', 'Иванова', 'Ленина, 15', '12345678900', 'только тише'),
                              ('Иван', 'Петров', 'Советская, 22', '98765432100', 'звоните дольше - я глухой')
                              ])
    def test_create_order(self, name, surname, adress, phone_number, comment, driver):
        order_page = OrderPage(driver)
        order_page.close_cookie()
        order_page.driver.get(ORDER_PAGE_URL)
        order_page.timeout(OrderPageLocators.name_input)
        order_page.fill_name(name)
        order_page.fill_surname(surname)
        order_page.fill_adress(adress)
        order_page.choose_metro_station()
        order_page.fill_phone_number(phone_number)
        order_page.go_on_btn_click()
        order_page.delivery_date_choose()
        order_page.rental_period_choose()
        order_page.black_color_choose()
        order_page.fill_comment(comment)
        order_page.create_order_btn_click()
        order_page.timeout(OrderPageLocators.confirm_orger_btn)
        order_page.confirm_orger_btn_click()
        assert order_page.check_check_status_btn_is_displayed()
