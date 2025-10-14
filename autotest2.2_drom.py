import pickle
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

chrome_options = Options()
chrome_options.add_argument("--profile-directory=Profile 2")

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://auto.drom.ru")

# pickle.dump(driver.get_cookies(), open("cookies.pkl","wb"))

cookies = pickle.load(open("cookies.pkl", "rb"))
for cookie in cookies:
    driver.add_cookie(cookie)

button_login = driver.find_element_by_xpath("//a[text()='Вход']").click()

login_text = driver.find_element_by_name('sign').send_keys('login')  # yatkinma@gmail.com

password_text = driver.find_element_by_name('password').send_keys('password')  # [jxedlhjv

button_sing = driver.find_element_by_id('signbutton').click()

add_to_favorites = driver.find_element_by_xpath(
    '/html/body/div[2]/div[5]/div[1]/div[1]/div[10]/div/div[2]/a[1]/div[3]/div[3]').click()

driver.quit()
