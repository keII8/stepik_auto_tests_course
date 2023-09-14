from selenium.webdriver.common.by import By
import time
from selenium import webdriver
import os

brow = webdriver.Chrome()
link = 'http://suninjuly.github.io/file_input.html'

try:
    brow.get(link)

    first = brow.find_element(By.CSS_SELECTOR, '[name="firstname"]')
    first.send_keys('Sergey')

    last_name = brow.find_element(By.CSS_SELECTOR, '[name="lastname"]')
    last_name.send_keys('Rybin')

    email = brow.find_element(By.CSS_SELECTOR, '[name="email"]')
    email.send_keys('sergeyrybin@mail.ru')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'lessons.txt')  # добавляем к этому пути имя файла
    file = brow.find_element(By.ID, 'file')
    file.send_keys(file_path)

    button = brow.find_element(By.TAG_NAME, 'button')
    button.click()


finally:
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    brow.quit()
