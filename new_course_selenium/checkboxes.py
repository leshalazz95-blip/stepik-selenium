import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

# Инициализация браузера (пример для Chrome)
browser = webdriver.Chrome()

try:
    # 1. Открываем страницу
    browser.get("https://suninjuly.github.io/math.html")

    # 2. Считываем значение переменной x
    x_element = browser.find_element(By.CSS_SELECTOR, "#input_value")
    x = x_element.text

    # 3. Считаем математическую функцию
    y = calc(x)

    # 4. Вводим ответ в текстовое поле
    answer_input = browser.find_element(By.CSS_SELECTOR, "#answer")
    answer_input.send_keys(y)

    # 5. Отмечаем checkbox "I'm the robot"
    robot_checkbox = browser.find_element(By.CSS_SELECTOR, "#robotCheckbox")
    robot_checkbox.click()

    # 6. Выбираем radiobutton "Robots rule!"
    robots_rule_radio = browser.find_element(By.CSS_SELECTOR, "#robotsRule")
    robots_rule_radio.click()

    # 7. Нажимаем на кнопку Submit
    submit_button = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    submit_button.click()

finally:
    # Небольшая пауза, чтобы увидеть результат (для отладки)
    import time
    time.sleep(10)
    browser.quit()