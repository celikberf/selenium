import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome()

url = "http://github.com"

driver.get(url)

searchInput= driver.find_element(By.XPATH, '"//*[@id="query-builder-test"]"')
time.sleep(1)
searchInput.send_keys("python")
time.sleep(2)
searchInput.send_keys(Keys.ENTER)
time.sleep(2)
result = driver.find_element(By.CSS_SELECTOR, ".Box-sc-g0xbh4-0 MHoGG search-title a")

for element in result:
    print(element.text)


driver.close()