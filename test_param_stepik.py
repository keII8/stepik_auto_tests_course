import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math


@pytest.mark.parametrize('link', ['https://stepik.org/lesson/236895/step/1',
                                'https://stepik.org/lesson/236896/step/1',
                                'https://stepik.org/lesson/236897/step/1',
                                'https://stepik.org/lesson/236898/step/1',
                                'https://stepik.org/lesson/236899/step/1',
                                'https://stepik.org/lesson/236903/step/1]',
                                'https://stepik.org/lesson/236904/step/1',
                                'https://stepik.org/lesson/236905/step/1'])
def test_authorization(browser, load_person_date, link):

    login = load_person_date['login_stepik']
    password = load_person_date['password_stepik']
    answer = math.log(int(time.time()))

    browser.get(link)                # Переходим по ссылке

    login_btn = browser.find_element(By.LINK_TEXT, 'Войти')
    login_btn.click()         # Нажимаем кнопку ВОЙТИ

    login_field = browser.find_element(By.XPATH, '//input[@name="login"]')
    login_field.send_keys(login) # Вводим логин

    password_field = browser.find_element(By.XPATH, '//input[@name="password"]')
    password_field.send_keys(password) # Вводим пароль


    btn = browser.find_element(By.XPATH, '//button[@type="submit"]')
    btn.click()

    input_txt = browser.find_element(By.CSS_SELECTOR, 'div > textarea').send_keys(str(answer))

    send_answer = browser.find_element(By.CLASS_NAME, 'submit-submission')
    send_answer.click()

    control_field = browser.find_element(By.CSS_SELECTOR, 'p .smart-hints__hint').text

    print(control_field)

    assert control_field == 'Correct!', 'Ошибка! Текст не соответсвует слову Correct!'


