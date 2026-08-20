import allure
import pytest
from tests.conftest import ORDER_DATA
from pages.order_page import OrderPage

@allure.story("Тесты заказа самоката")
class TestOrder:

    @pytest.mark.parametrize("order_data, button_position", [
        (ORDER_DATA[0], "верхнюю"),
        (ORDER_DATA[1], "нижнюю")
    ])
    def test_create_order(self, main_page, driver, order_data, button_position):
        with allure.step(f"Нажать кнопку заказа ({button_position})"):
            if button_position == "верхнюю":
                main_page.click_order_button_top()
            else:
                main_page.click_order_button_bottom()

        with allure.step("Заполнить форму заказа"):
            order_page = OrderPage(driver)
            order_page.fill_first_form(
                order_data["name"],
                order_data["surname"],
                order_data["address"],
                order_data["metro"],
                order_data["phone"]
            )
            order_page.fill_second_form(
                order_data["date"],
                order_data["comment"],
                order_data["color"]
            )

        with allure.step("Нажать кнопку 'Заказать'"):
            order_page.click_order_button()
            order_page.confirm_order()

        with allure.step("Проверить, что заказ оформлен"):
            assert order_page.is_order_success(), "Заказ не был оформлен"