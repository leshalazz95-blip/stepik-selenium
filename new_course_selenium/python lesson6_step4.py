import math
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

link = "http://suninjuly.github.io/find_link_text"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Вычисляем текст ссылки
    link_text = str(math.ceil(math.pow(math.pi, math.e) * 10000))
    print(f"Ищем ссылку с текстом: {link_text}")

    # 2. Находим ссылку по тексту и кликаем
    link_element = browser.find_element(By.LINK_TEXT, link_text)
    link_element.click()
    print("Перешли на форму регистрации")

    # 3. Заполняем форму
    browser.find_element(By.TAG_NAME, "input").send_keys("Ivan")
    browser.find_element(By.NAME, "last_name").send_keys("Petrov")
    browser.find_element(By.CLASS_NAME, "city").send_keys("Smolensk")
    browser.find_element(By.ID, "country").send_keys("Russia")

    # 4. Ждём, пока кнопка станет enabled, и кликаем
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button.btn"))
    )
    button.click()

    # 5. Читаем код из alert
    WebDriverWait(browser, 10).until(EC.alert_is_present())
    alert = browser.switch_to.alert
    code = alert.text
    print(f"\n\n>>> VERIFICATION CODE: {code} <<<\n\n")
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()