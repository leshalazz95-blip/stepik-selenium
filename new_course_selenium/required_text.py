import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    # 1. Ждём, пока цена не станет $100 (таймаут 15 секунд)
    WebDriverWait(browser, 15).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )

    # 2. Нажимаем Book
    browser.find_element(By.ID, "book").click()

    # 3. Решаем капчу
    x = browser.find_element(By.ID, "input_value").text
    y = calc(x)

    browser.find_element(By.ID, "answer").send_keys(y)

    # 4. Нажимаем Submit — используем ID "solve", а не button.btn,
    #    чтобы не поймать кнопку Book
    browser.find_element(By.ID, "solve").click()

    # 5. Забираем число из alert
    alert = browser.switch_to.alert
    print("Число из alert:", alert.text)
    alert.accept()

finally:
    time.sleep(5)
    browser.quit()