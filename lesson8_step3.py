from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12 * math.sin(x))))

    # кликаем по кнопке
    input1 = browser.find_element(By.CLASS_NAME, "btn")
    input1.click()
    # отрабатываем alert
    alert = browser.switch_to.alert
    alert.accept()

    # находим значение х
    x_element = browser.find_element(By.ID, "input_value")
    # вычисляем
    y = calc(int(x_element.text))
    # передаем значение в поле
    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
