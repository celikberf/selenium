from selenium import webdriver
import time

driver = webdriver.Chrome()

url = "http://github.com"

driver.get(url)

time.sleep(2)

driver.maximize_window()# sayfa 2saniye sonra tam ekran olur 

driver.save_screenshot("github.com-homepage.jpg")

url = "http://github.com/celikberf" # celikberf sayfasına git
driver.get(url)

print(driver.title)

if "celikberf" in driver.title:
    driver.save_screenshot("github-celikberf.png")

driver.back()
#driver.forward()

time.sleep(2)

driver.close() # sayfa 2 saniye sonra kapandı


