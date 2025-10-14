from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math, time

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/explicit_wait2.html")

    def calc(x):
        return str(math.log(abs(12 * math.sin(x))))

    button = browser.find_element(By.ID, "book")
    # # говорим WebDriver искать каждый элемент в течение 5 секунд
    # browser.implicitly_wait(5)

    bt = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "$100")
    )
    button.click()

    # вычисляем
    y = calc(int(browser.find_element(By.ID, "input_value").text))

    input2 = browser.find_element(By.ID, "answer").send_keys(y)
    button = browser.find_element(By.ID, "solve").click()


finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()
# assert "successful" in message.text
