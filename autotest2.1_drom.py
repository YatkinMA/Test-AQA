import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://auto.drom.ru")

brand = driver.find_element_by_xpath(
    '//input[@placeholder="Марка"]')
brand.click()
brand.send_keys("Toyota")
time.sleep(1)
brand.send_keys(Keys.RETURN)

time.sleep(1)
model = driver.find_element_by_xpath(
    '//input[@placeholder="Модель"]')
model.click()
time.sleep(1)
model.send_keys("Harrier")
time.sleep(1)
model.send_keys(Keys.RETURN)

fuel = driver.find_element_by_xpath(
    '//button[text()="Топливо"]')
fuel.click()
fuel_hybrid = driver.find_element_by_xpath(
    '//div[text()="Гибрид"]')
fuel_hybrid.click()

driver.find_element_by_xpath(
    '//label[@for="sales__filter_unsold"]').click()

year_car_min = driver.find_element_by_xpath(
    '//div[@data-ftid="sales__filter_year-from"]//button')
year_car_min.click()
year_car_min_2007 = driver.find_element_by_xpath(
    '//div[@data-ftid="sales__filter_year-from"]//div[text()="2007"]').click()

advanced_setting = driver.find_element_by_xpath(
    '//div[contains (@class,"css-mwckxy evnwjo70") and contains (., "Расширенный поиск")]').click()

mileage_min = driver.find_element_by_xpath(
    '//input[@data-ftid="sales__filter_mileage-from"]')
mileage_min.click()
mileage_min.send_keys('1', Keys.RETURN)


def getComputedStyle(element):
    return driver.execute_script('var items = {};' +
                                 'var compsty = getComputedStyle(arguments[0]);' +
                                 'var len = compsty.length;' +
                                 'for (index = 0; index < len; index++)' +
                                 '{items [compsty[index]] = compsty.getPropertyValue(compsty[index])};' +
                                 'return items;', element)


def assert_items():
    items = driver.find_elements_by_xpath('//a[@data-ftid="bulls-list_bull"]')
    for item in items:
        title = item.find_element_by_xpath('.//span[@data-ftid="bull_title"]/..')
        style = getComputedStyle(title).get('text-decoration')
        assert "line-through" not in style
        year = int(title.text.split(', ')[1])
        assert year >= 2007
        description = item.find_element_by_xpath('.//div[@data-ftid="component_inline-bull-description"]')
        assert "тыс. км" in description.text


assert_items()

driver.find_element_by_xpath(' //a[@data-ftid="component_pagination-item-next"]').click()

assert_items()

driver.close()
