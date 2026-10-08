import os
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

link = "http://suninjuly.github.io/file_input.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Заполняем текстовые поля
    browser.find_element(By.NAME, "firstname").send_keys("Ivan")
    browser.find_element(By.NAME, "lastname").send_keys("Petrov")
    browser.find_element(By.NAME, "email").send_keys("ivan@example.com")

    # 2. Создаём пустой .txt-файл рядом со скриптом
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, "test_file.txt")

    with open(file_path, "w") as f:
        f.write("some content")  # можно и пустой: pass

    # 3. Загружаем файл — просто send_keys с путём к файлу
    upload_input = browser.find_element(By.ID, "file")
    upload_input.send_keys(file_path)

    # 4. Нажимаем Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()