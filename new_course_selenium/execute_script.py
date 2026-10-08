import math
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "https://suninjuly.github.io/execute_script.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Считываем x
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    # 2. Вводим ответ
    browser.find_element(By.ID, "answer").send_keys(y)

    # 3. Checkbox "I'm the robot" — скроллим перед кликом
    robot_checkbox = browser.find_element(By.ID, "robotCheckbox")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robot_checkbox)
    robot_checkbox.click()

    # 4. Radiobutton "Robots rule!" — скроллим перед кликом
    robots_radio = browser.find_element(By.ID, "robotsRule")
    browser.execute_script("return arguments[0].scrollIntoView(true);", robots_radio)
    robots_radio.click()

    # 5. Submit — скроллим перед кликом
    submit_button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    browser.execute_script("return arguments[0].scrollIntoView(true);", submit_button)
    submit_button.click()

finally:
    time.sleep(10)
    browser.quit()