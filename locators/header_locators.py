from selenium.webdriver.common.by import By


class HeaderLocators:
    ya_logo = [By.CLASS_NAME, "Header_LogoYandex__3TSOI"]  # логотип Яндекс
    scooter_logo = [By.XPATH, "//a[contains(@class, 'Header_LogoScooter')]"]  # логотип Самокат
    order_header_btn = [By.XPATH, "//div[contains(@class, 'Header')]/button[text() = 'Заказать']"]  # кнопка заказать
    order_status_btn = [By.XPATH,
                        "//div[contains(@class, 'Header')]/button[text() = 'Статус заказа']"]  # Кнопка Статус заказа
    go_btn = [By.XPATH, "//button[text() = 'Go!']"]  # Кнопка Go!
    order_number_input = [By.XPATH, "//input[@placeholder = 'Введите номер заказа']"]  # поле ввода номера заказа
    close_cookie_btn = (By.XPATH, "//button[text() = 'да все привыкли']")  # кнопка принятия куки
