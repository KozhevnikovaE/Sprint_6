from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import allure

BASE_URL = "https://qa-scooter.praktikum-services.ru/"


class MainPage(BasePage):
    # Локаторы
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BUTTON_BOTTOM = (By.CSS_SELECTOR, 'button[class*="Button"]')
    FAQ_QUESTIONS = (By.CSS_SELECTOR, '.accordion__button')
    LOGO_SAMOKAT = (By.CSS_SELECTOR, 'a img[alt="Scooter"]')
    LOGO_YANDEX = (By.CSS_SELECTOR, 'a img[alt="Yandex"]')

    @allure.step("Открыть главную страницу")
    def open(self):
        self.get_url(BASE_URL)

    @allure.step("Принять cookies")
    def accept_cookies(self):
        """Нажимает кнопку куки, если она есть. Не падает, если её нет."""
        try:
            self.click_element(self.COOKIE_BUTTON)
        except Exception:
            pass


    @allure.step("Нажать кнопку заказа вверху страницы")
    def click_order_button_top(self):
        self.click_element(self.ORDER_BUTTON_TOP)

    @allure.step("Нажать кнопку заказа внизу страницы")
    def click_order_button_bottom(self):
        button = self.find_element(self.ORDER_BUTTON_BOTTOM)
        self.scroll_to_element(button)
        self.click_element(self.ORDER_BUTTON_BOTTOM)


    @allure.step("Кликнуть на вопрос")
    def click_faq_question(self, index):
        questions = self.find_elements(self.FAQ_QUESTIONS)
        question = questions[index]
        self.scroll_to_element(question)
        self.driver.execute_script("arguments[0].click();", question)


    @allure.step("Получить ответ на вопрос")
    def get_faq_answer(self, index):
        answer_locator = (By.XPATH, f"//div[@id='accordion__panel-{index}']/p")
        answer = self.wait.until(EC.visibility_of_element_located(answer_locator))
        return answer.text

    @allure.step("Кликнуть на логотип 'Самокат'")
    def click_samokat_logo(self):
        self.click_element(self.LOGO_SAMOKAT)

    
    @allure.step("Кликнуть на логотип 'Яндекс'")
    def click_yandex_logo(self):
        self.click_element(self.LOGO_YANDEX)



    @allure.step("Дождаться перехода на главную страницу")
    def wait_for_main_url(self, timeout=5):
        return WebDriverWait(self.driver, timeout).until(EC.url_to_be(BASE_URL))

    @allure.step("Кликнуть логотип Яндекса и переключиться на Дзен")
    def click_yandex_logo_and_switch_to_dzen(self, timeout=10):
        self.click_yandex_logo()
        tabs = self.get_window_handles()
        self.switch_to_window(tabs[1])
        return WebDriverWait(self.driver, timeout).until(EC.url_contains("dzen.ru"))

    @allure.step("Закрыть вкладку Дзена и вернуться обратно")
    def close_extra_tab_and_return(self):
        tabs = self.get_window_handles()
        self.close_window()
        self.switch_to_window(tabs[0])