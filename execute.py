from selenium.webdriver.common.by import By
import time
from selenium import webdriver

import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))



browser = webdriver.Chrome()
link = "http://suninjuly.github.io/execute_script.html"

try:
    browser.get(link)

    x = int(browser.find_element(By.ID, 'input_value').text)


    answer = browser.find_element(By.ID, "answer")
    browser.execute_script("return arguments[0].scrollIntoView(true);", answer)
    answer.send_keys(calc(x))

    check = browser.find_element(By.ID, 'robotCheckbox')
    check.click()

    radio = browser.find_element(By.ID, 'robotsRule')
    radio.click()

    button = browser.find_element(By., 'button')
    button.click()


finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
