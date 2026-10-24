import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class TestRegistration(unittest.TestCase):

    def test_registration1(self):
        """Тест для страницы registration1.html — должен пройти успешно."""
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration1.html")

        browser.find_element(By.CSS_SELECTOR, "input.first[placeholder='Input your first name']").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, "input.second[placeholder='Input your last name']").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, "input.third[placeholder='Input your email']").send_keys("ivan@example.com")

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)

        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        browser.quit()

        self.assertEqual(
            "Congratulations! You have successfully registered!",
            welcome_text,
            "Registration failed"
        )

    def test_registration2(self):
        """Тест для страницы registration2.html — должен упасть с NoSuchElementException."""
        browser = webdriver.Chrome()
        browser.get("http://suninjuly.github.io/registration2.html")

        browser.find_element(By.CSS_SELECTOR, "input.first[placeholder='Input your first name']").send_keys("Ivan")
        browser.find_element(By.CSS_SELECTOR, "input.second[placeholder='Input your last name']").send_keys("Petrov")
        browser.find_element(By.CSS_SELECTOR, "input.third[placeholder='Input your email']").send_keys("ivan@example.com")

        browser.find_element(By.CSS_SELECTOR, "button.btn").click()
        time.sleep(1)

        welcome_text = browser.find_element(By.TAG_NAME, "h1").text
        browser.quit()

        self.assertEqual(
            "Congratulations! You have successfully registered!",
            welcome_text,
            "Registration failed"
        )


if __name__ == "__main__":
    unittest.main()