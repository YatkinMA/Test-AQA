import time
from selenium import webdriver

driver = webdriver.Chrome()
driver.get("https://auto.drom.ru/region25/")

driver.find_element_by_xpath(
    '//a[contains(@class, "css-17f5zdi") and contains(., "Другой город")]').click()
time.sleep(1)
driver.find_element_by_xpath(
    '//div[contains(@class, "css-19r61") and [contains](., "Приморский край")]').click()
driver.find_element_by_xpath(
    '//div[contains(@class, "css-1s8kstr") and contains(., "Все города региона")]').click()
driver.find_element_by_xpath("//div[text()='Показать все']").click()
list_product = driver.find_elements_by_xpath(
    '//div[@data-ftid="component_cars-list"]//div[@class="css-pvjszw e4ojbx44"]')
res = []
for div in list_product:
    spans = div.find_elements_by_xpath('./span')
    res.append([(int(spans[1].text)), spans[0].text])

res = sorted(res, reverse=True)[:20]
print('| Фирма | Количество объявлений |')
for r in res:
    print(f'| {r[1]} | {r[0]} |')

driver.close()
