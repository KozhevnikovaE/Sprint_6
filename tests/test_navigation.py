import allure

@allure.story("Тесты навигации")
class TestNavigation:

    @allure.title("Проверка перехода на главную страницу по клику на логотип 'Самокат'")
    def test_click_samokat_logo(self, main_page):
        with allure.step("Нажать кнопку заказа"):
            main_page.click_order_button_top()

        with allure.step("Кликнуть на логотип 'Самокат'"):
            main_page.click_samokat_logo()

        with allure.step("Проверить, что открылась главная страница"):
            assert main_page.wait_for_main_url(), "Не удалось перейти на главную страницу"

    @allure.title("Проверка перехода на Дзен по клику на логотип 'Яндекс'")
    def test_click_yandex_logo(self, main_page):
        with allure.step("Кликнуть на логотип 'Яндекс'и переключиться на новую вкладку"):
            is_dzen_opened = main_page.click_yandex_logo_and_switch_to_dzen()

        with allure.step("Проверить, что открылся Дзен"):
            assert is_dzen_opened, "Не удалось перейти на Дзен"

        with allure.step("Закрыть окно Дзена и вернуться обратно"):
            main_page.close_extra_tab_and_return()