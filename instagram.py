from instagramUserInfo import username,password
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

class Instagram:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password

    def signIn(self):
        self.browser.get("https://www.instagram.com/")
        time.sleep(3)
        usernameInput = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div[1]/div[1]/div/label/input")
        passwordInput = self.browser.find_element(By.XPATH, "//*[@id='loginForm']/div[1]/div[2]/div/label/input")

        usernameInput.send_keys(self.email)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(10)

    def getFollowers(self):
        self.browser.get("http://www.instagram.com/celikberf/followers")
        time.sleep(10)
        followersLink = self.browser.find_element(By.XPATH, "//*[@id='mount_0_0_dw']/div/div/div[2]/div/div/div[1]/div[2]/div/div[1]/section/main/div/header/section[3]/ul/li[2]/div/a/span/span")
        followersLink.click()

instgrm = Instagram(username,password)
instgrm.signIn()
instgrm.getFollowers()