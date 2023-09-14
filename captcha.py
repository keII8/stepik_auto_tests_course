

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

import time


try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/selects1.html")

    num1 = browser.find_element(By.ID, 'num1')
    num2 = browser.find_element(By.ID, 'num2')
    x = int(num1.text) + int(num2.text)

    select1 = Select(browser.find_element(By.TAG_NAME, "select"))
    select1.select_by_value(str(x))


    # input1 = browser.find_element(By.ID, "answer")
    # input1.send_keys(y)
    #
    # option1 = browser.find_element(By.ID, "robotCheckbox")
    # option1.click()
    #
    # option2 = browser.find_element(By.ID, "robotsRule")
    # option2.click()

    button = browser.find_element(By.TAG_NAME, 'button')
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()