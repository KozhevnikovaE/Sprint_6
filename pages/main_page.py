from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
from tests.url import BASE_URL


class MainPage(BasePage):
    # Локаторы
    COOKIE_BUTTON = (By.ID, "rcc-confirm-button")
    ORDER_BUTTON_TOP = (By.CLASS_NAME, "Button_Button__ra12g")
    ORDER_BUTTON_BOTTOM = (By.CSS_SELECTOR, 'button[class*="Button"]')
    FAQ_QUESTIONS = (By.CSS_SELECTOR, '.accordion__button')
    LOGO_SAMOKAT = (By.CSS_SELECTOR, 'a img[alt="Scooter"]')
    LOGO_YANDEX = (By.CSS_SELECTOR, 'a img[alt="Yandex"]')


    def open(self):
        self.driver.get(BASE_URL)
        return self

    def accept_cookies(self):
        """Нажимает кнопку куки, если она есть. Не падает, если её нет."""
        try:
            self.click_element(self.COOKIE_BUTTON)
        except Exception:
            pass
        return self

    def click_order_button_top(self):
        self.click_element(self.ORDER_BUTTON_TOP)

    def click_order_button_bottom(self):
        button = self.find_element(self.ORDER_BUTTON_BOTTOM)
        self.scroll_to_element(button)
        self.click_element(self.ORDER_BUTTON_BOTTOM)
        return self

    def click_faq_question(self, index):
        questions = self.find_elements(self.FAQ_QUESTIONS)
        question = questions[index]
        self.scroll_to_element(question)
        
        self.driver.execute_script("arguments[0].click();", question)
        return self

    def get_faq_answer(self, index):
        answer_locator = (By.XPATH, f"//div[@id='accordion__panel-{index}']/p")
        answer = self.wait.until(EC.visibility_of_element_located(answer_locator))
        return answer.text

    def click_samokat_logo(self):
        self.click_element(self.LOGO_SAMOKAT)
        return self
    
    def click_yandex_logo(self):
        self.click_element(self.LOGO_YANDEX)
        return self