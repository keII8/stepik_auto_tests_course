import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome()
welcome_text_true = 'Congratulations! You have successfully registered!'
class TestRegistration(unittest.TestCase):
    def test_registration_correct(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)
            # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'name')]")
        input1.send_keys('Ivan')
        input2 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'last name')]")
        input2.send_keys('Ivanov')
        input3 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]")
        input3.send_keys('pochta@mail.sup')
            # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)
            # находим элемент, содержащий текст
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(welcome_text, welcome_text_true, "Ошибка регистрации")

    def test_registration_fail(self):
        link = "https://suninjuly.github.io/registration2.html"
        browser.get(link)
        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'name')]")
        input1.send_keys('Ivan')
        input2 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'last name')]")
        input2.send_keys('Ivanov')
        input3 = browser.find_element(By.XPATH, "//input[contains(@placeholder, 'email')]")
        input3.send_keys('pochta@mail.sup')
        # Отправляем заполненную форму
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        self.assertEqual(welcome_text, welcome_text_true, "Ошибка регистрации")


if __name__ == "__main__":
    unittest.main()