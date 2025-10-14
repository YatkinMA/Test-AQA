from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import math
import os

try: 
    link = "http://suninjuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    def calc(x):
        return str(math.log(abs(12*math.sin(int(x)))))

    x = browser.find_element(By.CSS_SELECTOR, "#input_value")

    y = calc(x.text)
    
    input1 = browser.find_element(By.ID, "answer")
    input1.send_keys(y)
    # browser.execute_script("return arguments[0].scrollIntoView(true);", input1)
    browser.execute_script("document.getElementById('answer').scrollIntoView(true);")
    input2 = browser.find_element(By.ID, "robotCheckbox")
    input2.click()
    input3 = browser.find_element(By.ID, "robotsRule")
    input3.click()
    

    # Отправляем заполненную форму
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
    time.sleep(1)
    print(os.path.abspath(__file__))
    print(os.path.abspath(os.path.dirname(__file__)))

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
    