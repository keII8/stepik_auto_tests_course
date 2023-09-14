from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import math
import time


browser = webdriver.Chrome()

link = 'http://suninjuly.github.io/selects2.html'

try:
    browser.get(link)

    num_1 = browser.find_element(By.ID, 'num1').text
    num_2 = browser.find_element(By.ID, 'num2').text



    total = int(num_1) + int(num_2)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(str(total))

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    time.sleep(10)
    browser.quit()

