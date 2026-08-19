import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

@allure.story("Тесты навигации")
class TestNavigation:

    @allure.title("Проверка перехода на главную страницу по клику на логотип 'Самокат'")
    def test_click_samokat_logo(self, main_page, driver):
        with allure.step("Нажать кнопку заказа"):
            main_page.click_order_button_top()

        with allure.step("Кликнуть на логотип 'Самокат'"):
            main_page.click_samokat_logo()

        with allure.step("Проверить, что открылась главная страница"):
            wait = WebDriverWait(driver, 5)
            is_main_page = wait.until(EC.url_to_be("https://qa-scooter.praktikum-services.ru/"))
            assert is_main_page, "Не удалось перейти на главную страницу"

    @allure.title("Проверка перехода на Дзен по клику на логотип 'Яндекс'")
    def test_click_yandex_logo(self, main_page, driver):
        with allure.step("Кликнуть на логотип 'Яндекс'"):
            main_page.click_yandex_logo()

        with allure.step("Переключиться на новое окно"):
            tabs = driver.window_handles
            driver.switch_to.window(tabs[1])

        with allure.step("Проверить, что открылся Дзен"):
            wait = WebDriverWait(driver, 10)
            is_dzen_opened = wait.until(EC.url_contains("dzen.ru"))
            assert is_dzen_opened, "Не удалось перейти на Дзен"

        with allure.step("Закрыть окно Дзена и вернуться обратно"):
            driver.close()
            driver.switch_to.window(tabs[0])