from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

link = "https://suninjuly.github.io/selects1.html"  # или selects2.html

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Считываем оба числа со страницы
    num1 = browser.find_element(By.ID, "num1").text
    num2 = browser.find_element(By.ID, "num2").text

    # 2. Считаем сумму (числа приходят строками!)
    total = str(int(num1) + int(num2))

    # 3. Выбираем значение в выпадающем списке по видимому тексту
    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_visible_text(total)

    # 4. Нажимаем Submit
    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    time.sleep(10)
    browser.quit()