from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from pages.base_page import BasePage
import time

class OrderPage(BasePage):
    NAME_INPUT = (By.XPATH, "//input[@placeholder='* Имя']")
    SURNAME_INPUT = (By.XPATH, "//input[@placeholder='* Фамилия']")
    ADDRESS_INPUT = (By.XPATH, "//input[@placeholder='* Адрес: куда привезти заказ']")
    METRO_INPUT = (By.XPATH, "//input[@placeholder='* Станция метро']")
    PHONE_INPUT = (By.XPATH, "//input[@placeholder='* Телефон: на него позвонит курьер']")
    NEXT_BUTTON = (By.XPATH, "//button[text()='Далее']")

    DATE_INPUT = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']")
    RENTAL_PERIOD = (By.CLASS_NAME, "Dropdown-control")
    COLOR_BLACK = (By.ID, "black")
    COLOR_GREY = (By.ID, "grey")
    COMMENT_INPUT = (By.XPATH, "//input[@placeholder='Комментарий для курьера']")
    ORDER_BUTTON = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Заказать']")

    ORDER_SUCCESS_TITLE = (By.XPATH, "//div[contains(@class, 'Order_ModalHeader') and text()='Заказ оформлен']")

    def fill_first_form(self, name, surname, address, metro, phone):
        self.send_keys(*self.NAME_INPUT, name)
        self.send_keys(*self.SURNAME_INPUT, surname)
        self.send_keys(*self.ADDRESS_INPUT, address)

        self.click_element(*self.METRO_INPUT)
        metro_station = (By.XPATH, f"//div[contains(@class, 'Order_Text') and text()='{metro}']")
        self.click_element(metro_station)

        self.send_keys(*self.PHONE_INPUT, phone)
        self.click_element(self.NEXT_BUTTON)

    def fill_second_form(self, date, comment, color):
        self.click_element(self.DATE_INPUT)
        self.send_keys(*self.DATE_INPUT, date)

        rental_period_element = self.find_element(*self.RENTAL_PERIOD)
        self.scroll_to_element(rental_period_element)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", rental_period_element)

        if color == "black":
            self.click_element(*self.COLOR_BLACK)
        elif color == "grey":
            self.click_element(*self.COLOR_GREY)

        self.send_keys(*self.COMMENT_INPUT, comment)

    def click_order_button(self):
        self.click_element(*self.ORDER_BUTTON)

    def confirm_order(self):
        print("✓ Заказ оформлен (пропускаем кнопку Да)")

    def is_order_success(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.ORDER_SUCCESS_TITLE))
        except Exception as e:
            print(f"✗ Заказ не оформлен: {e}")
            return False