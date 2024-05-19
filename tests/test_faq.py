import allure
import pytest
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators


class TestFaqPage:
    faq_content = [
        (MainPageLocators.question1, MainPageLocators.answer1, 'Сутки — 400 рублей. Оплата курьеру — наличными или '
                                                               'картой.'),
        (MainPageLocators.question2, MainPageLocators.answer2,
         'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями,'
         ' можете просто сделать несколько заказов — один за другим.'),
        (MainPageLocators.question3, MainPageLocators.answer3, 'Допустим, вы оформляете заказ на 8 мая. ' 
         'Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы '
         'оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.'),
        [MainPageLocators.question4, MainPageLocators.answer4, 'Только начиная с завтрашнего дня. Но скоро станем '
                                                               'расторопнее.'],
        [MainPageLocators.question5, MainPageLocators.answer5,
         'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.'],
        [MainPageLocators.question6, MainPageLocators.answer6, 'Самокат приезжает к вам с полной зарядкой. '
                                                               'Этого хватает на восемь суток — даже если будете '
                                                               'кататься без передышек и во сне. Зарядка не '
                                                               'понадобится.'],
        [MainPageLocators.question7, MainPageLocators.answer7,
         'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.'],
        [MainPageLocators.question8, MainPageLocators.answer8,
         'Да, обязательно. Всем самокатов! И Москве, и Московской области.']
    ]

    @allure.description('параметризованный тест для проверки соответствия каждого ответа вопросу')
    @allure.title('проверка соответствия ответа вопросу в разделе Вопросы о важном')
    @pytest.mark.parametrize('question_locator,answer_locator,answer', faq_content)
    def test_check_right_answer(self, question_locator, answer_locator, answer, driver):
        main_page = MainPage(driver)
        main_page.timeout(question_locator)
        main_page.question_click(question_locator)
        main_page.timeout(answer_locator)
        real_answer = main_page.get_answer_text(answer_locator)
        assert real_answer == answer
