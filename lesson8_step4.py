from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(x))))

    # кликаем по кнопке
    input1 = browser.find_element(By.CLASS_NAME, "trollface").click()

    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)

    # находим значение х
    x_element = browser.find_element(By.ID, "input_value")
    # вычисляем
    y = calc(int(x_element.text))
    # передаем значение в поле
    input2 = browser.find_element(By.ID, "answer").send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
