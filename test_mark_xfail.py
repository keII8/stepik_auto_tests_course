import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

link = "http://selenium1py.pythonanywhere.com/"

class TestMainPage1():

    def test_guest_should_see_login_link(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "#login_link")

    def test_guest_should_see_basket_link_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, ".basket-mini .btn-group > a")

    @pytest.mark.xfail    # Отметка о том что кейс с багом, также можно добавить комментарий с помщью  @pytest.mark.xfail(reason="fixing this bug right now")
    def test_guest_should_see_search_button_on_the_main_page(self, browser):
        browser.get(link)
        browser.find_element(By.CSS_SELECTOR, "button.favorite")
        '''Когда баг починят, мы это узнаем,так как теперь тест будет отмечен как XPASS (“unexpectedly passing” — неожиданно проходит). 
        После этого маркировку xfail для теста можно удалить. Кстати, к маркировке xfail можно добавлять параметр reason. 
        Чтобы увидеть это сообщение в консоли, при запуске нужно добавлять параметр pytest -rx.'''

        # запуск для просмотра тестов с xpassed - pytest -rX -v test_fixture10b.py

