from selenium import webdriver
from selenium.webdriver.common.by import By
import time

try:
    link = "http://suninjuly.github.io/registration2.html"
    browser = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your first name']").send_keys("Ivan")
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your last name']").send_keys("Petrov")
    browser.find_element(By.CSS_SELECTOR, "[placeholder='Input your email']").send_keys("ivan@test.com")

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    time.sleep(1)

    welcome_text = browser.find_element(By.TAG_NAME, "h1").text
    assert "Congratulations! You have successfully registered!" == welcome_text

finally:
    time.sleep(10)
    browser.quit()