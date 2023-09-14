from selenium import webdriver
from selenium.webdriver.common.by import By
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/get_attribute.html'

try:
    browser.get(link)
    value_x = browser.find_element(By.ID, 'treasure')
    x = value_x.get_attribute('valuex')

    text = browser.find_element(By.ID, 'answer')
    text.send_keys(calc(x))

    check = browser.find_element(By.ID, 'robotCheckbox')
    check.click()

    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()
finally:
    time.sleep(10)
    browser.quit()

