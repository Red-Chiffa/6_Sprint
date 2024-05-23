from selenium.webdriver.common.by import By


class MainPageLocators:
    order_btn = (By.XPATH, "//div[contains(@class, 'Home')]/button[text() = 'Заказать']")  # кнопка Заказать
    # в блоке Как это работает
    faq_section = (By.CLASS_NAME, 'Home_FourPart__1uthg')  # Название раздела Вопросы о важном
    question1 = (By.XPATH, "//div[@data-accordion-component = 'AccordionItem'][1]")  # вопрос 1
    question2 = (By.XPATH, "//div[@data-accordion-component = 'AccordionItem'][2]")  # вопрос 2
    question3 = (By.XPATH, "//div[@data-accordion-component = 'AccordionItem'][3]")  # вопрос 3
    question4 = (By.XPATH, "//div[@data-accordion-component = 'AccordionItem'][4]")  # вопрос 4
    question5 = (By.XPATH, "//div[@data-accordion-component = 'AccordionItem'][5]")  # вопрос 5
    question6 = (By.XPATH, "//div[@data-accordion-component = 'AccordionItem'][6]")  # вопрос 6
    question7 = (By.XPATH, "//div[@data-accordion-component = 'AccordionItem'][7]")  # вопрос 7
    question8 = (By.XPATH, "//div[@data-accordion-component = 'AccordionItem'][8]")  # вопрос 8
    answer1 = (By.XPATH, "//*[@id='accordion__panel-0']")  # ответ 1
    answer2 = (By.XPATH, "//*[@id='accordion__panel-1']/p")  # ответ 2
    answer3 = (By.XPATH, "//*[@id='accordion__panel-2']/p")  # ответ 3
    answer4 = (By.XPATH, "//*[@id='accordion__panel-3']/p")  # ответ 4
    answer5 = (By.XPATH, "//*[@id='accordion__panel-4']/p")  # ответ 5
    answer6 = (By.XPATH, "//*[@id='accordion__panel-5']/p")  # ответ 6
    answer7 = (By.XPATH, "//*[@id='accordion__panel-6']/p")  # ответ 7
    answer8 = (By.XPATH, "//*[@id='accordion__panel-7']/p")  # ответ 8
    close_cookie_btn = (By.XPATH, "//button[text() = 'да все привыкли']")  # кнопка принятия куки
    cookie_button = (By.XPATH, "//*[@id='rcc-confirm-button']")  # кнопка принятия куки
