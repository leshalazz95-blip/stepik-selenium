import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Нажимаем кнопку, которая вызывает confirm
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # 2. Переключаемся на alert и принимаем его
    confirm = browser.switch_to.alert
    confirm.accept()

    # 3. На новой странице решаем капчу
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()