import time


def test_add_to_basket_button_is_present(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    browser.get(link)

    # Пауза для визуальной проверки языка интерфейса (для рецензента)
    time.sleep(30)

    # Уникальный селектор кнопки "Добавить в корзину" на этой странице
    button = browser.find_element("css selector", "button.btn-add-to-basket")

    assert button.is_displayed(), "Кнопка добавления в корзину не найдена на странице"