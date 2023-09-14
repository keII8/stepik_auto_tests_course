from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

browser = webdriver.Chrome()
link = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser.get(link)

    btn_1 = browser.find_element(By.TAG_NAME, 'button')
    btn_1.click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    x = int(browser.find_element(By.ID, 'input_value').text)

    answer = browser.find_element(By.ID, 'answer')
    answer.send_keys(calc(x))

    btn_2 = browser.find_element(By.TAG_NAME, 'button')
    btn_2.click()

finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()