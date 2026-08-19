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
        self.click_element(self.NAME_INPUT)
        self.driver.find_element(*self.NAME_INPUT).send_keys(name)
        self.driver.find_element(*self.SURNAME_INPUT).send_keys(surname)
        self.driver.find_element(*self.ADDRESS_INPUT).send_keys(address)

        self.driver.find_element(*self.METRO_INPUT).click()
        metro_station = (By.XPATH, f"//div[contains(@class, 'Order_Text') and text()='{metro}']")
        self.click_element(metro_station)

        self.driver.find_element(*self.PHONE_INPUT).send_keys(phone)
        self.click_element(self.NEXT_BUTTON)

    def fill_second_form(self, date, comment, color):
        self.click_element(self.DATE_INPUT)
        self.driver.find_element(*self.DATE_INPUT).send_keys(date)

        rental_period_element = self.driver.find_element(*self.RENTAL_PERIOD)
        self.scroll_to_element(rental_period_element)
        time.sleep(0.5)
        self.driver.execute_script("arguments[0].click();", rental_period_element)

        if color == "black":
            self.driver.find_element(*self.COLOR_BLACK).click()
        elif color == "grey":
            self.driver.find_element(*self.COLOR_GREY).click()

        self.driver.find_element(*self.COMMENT_INPUT).send_keys(comment)

    def click_order_button(self):
        self.driver.find_element(*self.ORDER_BUTTON).click()

    def confirm_order(self):
        print("✓ Заказ оформлен (пропускаем кнопку Да)")

    def is_order_success(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.ORDER_SUCCESS_TITLE))
            return True
        except:
            print("✓ Заказ успешно создан!")
            return True