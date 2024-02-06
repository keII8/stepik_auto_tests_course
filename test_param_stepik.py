import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class TestLogin:
    def test_authorization(self, browser, load_person_date):

        login = load_person_date['login_stepik']
        password = load_person_date['password_stepik']
        link = 'https://stepik.org/lesson/236895/step/1'

        browser.get(link)                # Переходим по ссылке

        login_btn = browser.find_element(By.XPATH, '//a[@href="/lesson/236895/step/1?auth=login"]')
        login_btn.click()         # Нажимаем кнопку ВОЙТИ

        login_field = browser.find_element(By.XPATH, '//input[@name="login"]')
        login_field.send_keys(login) # Вводим логин

        password_field = browser.find_element(By.XPATH, '//input[@name="password"]')
        password_field.send_keys(password) # Вводим пароль

        btn = browser.find_element(By.XPATH, '//button[@type="submit"]')
        btn.click()

        time.sleep(5)

