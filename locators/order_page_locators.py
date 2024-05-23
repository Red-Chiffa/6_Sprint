from selenium.webdriver.common.by import By


class OrderPageLocators:
    name_input = (By.XPATH, "//input[@placeholder='* Имя']")  # поле ввода Имени
    surname_input = (By.XPATH, "//input[@placeholder='* Фамилия']")  # поле ввода Фамилии
    adress_input = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")  # поле ввода Адреса
    metro_input = (By.CLASS_NAME, "select-search__input")  # дропдаун станиций метро
    metro_station_choose = (By.XPATH, "//div[@class = 'select-search__select'][1]")  # выбор станции метро
    phone_number_input = (By.XPATH,
                          "//input[@placeholder='* Телефон: на него позвонит курьер']")  # поле ввода номера телефона
    next_btn = (By.XPATH, "//button[text() = 'Далее']")  # кнопка Далее
    date_input = (By.XPATH, "//input[@placeholder = '* Когда привезти самокат']")  # поле ввода даты доставки
    calendar_choose_day = (
        By.XPATH, "//div[5]/div[contains(@class, 'react-datepicker__day ')][7]")  # выбор даты на календаре
    rental_period_input = (By.CLASS_NAME, "Dropdown-placeholder")  # дропдаун срока аренды
    rental_period = (By.XPATH, "//div[@class = 'Dropdown-menu']/div[text()='шестеро суток']")  # выбор срока аренды
    checkbox_black = (By.ID, "black")  # чек-бокс черного самоката
    checkbox_grey = (By.ID, "grey")  # чек-бокс серого самоката
    comment_input = (By.XPATH, "//input[@placeholder = 'Комментарий для курьера']")  # поле ввода комментария
    create_order_btn = (
        By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text() = 'Заказать']")  # кнопка Заказать
    confirm_orger_btn = (By.XPATH,
                         "//div[contains(@class, 'Order_Modal')]/div[2]/button[text() = 'Да']")  # кнопка Да на
    # всплывающем сообщении
    check_status = (
        By.XPATH, "//button[text() = 'Посмотреть статус']")  # кнопка Посмотреть статус на всплывающем сообщении
    cancel_order = (
        By.XPATH, "//button[text() = 'Отменить заказ']")  # кнопка Отменить заказ на странице информации о заказе
