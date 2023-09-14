from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser.get(link)

    btn = browser.find_element(By.TAG_NAME, 'button')
    btn.click()
    
    confirm = browser.switch_to.alert
    confirm.accept()

    x = int(browser.find_element(By.ID, 'input_value').text)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(calc(x))

    btn_1 = browser.find_element(By.TAG_NAME, 'button')
    btn_1.click()


finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()