import allure
from config import BASE_URL, YA_REDIRECT_URL, ORDER_PAGE_URL
from pages.header_page import HeaderPage
from pages.main_page import MainPage


class TestHeader:

    @allure.description('тест проверяет что при тапе на логотип Яндексе в хэдере происходит редирект на страницу '
                        'Яндекс.Дзен')
    @allure.title('редирект по клику на лого Яндекс')
    def test_ya_logo_click(self, driver):
        main_page = MainPage(driver)
        main_page.close_cookie()
        header_page = HeaderPage(driver)
        header_page.ya_logo_click()
        header_page.switch_to_window()
        header_page.timeout_url(YA_REDIRECT_URL)
        assert YA_REDIRECT_URL in header_page.get_current_url()

    @allure.description('тест проверяет, что при тапе на логотип Самокат в хэдере происходит переход на главную '
                        'страницу')
    @allure.title('клик по логотипу Самокат в хэдере')
    def test_scooter_logo_click(self, driver):
        main_page = MainPage(driver)
        main_page.close_cookie()
        header_page = HeaderPage(driver)
        header_page.order_header_btn_click()
        header_page.scooter_logo_click()
        assert BASE_URL in header_page.get_current_url()

    @allure.description('тест проверяет что при тапе на кнопку Заказать в хэдере происходит переход на страницу '
                        'оформлениея заказа')
    @allure.title('клик по кнопке Заказать в хэдере')
    def test_order_header_btn_click(self, driver):
        main_page = MainPage(driver)
        main_page.close_cookie()
        header_page = HeaderPage(driver)
        header_page.order_header_btn_click()
        assert ORDER_PAGE_URL in header_page.get_current_url()
