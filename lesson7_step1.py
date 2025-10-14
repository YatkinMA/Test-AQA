from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(num1, num2):
        return str(int(num1) + int(num2))

    x_element = browser.find_element(By.ID, "num1").text

    y_element = browser.find_element(By.ID, "num2").text

    y = calc(x_element, y_element)

    select = Select(browser.find_element(By.ID, "dropdown"))
    select.select_by_value(y)

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(15)
    # закрываем браузер после всех манипуляций
    browser.quit()
