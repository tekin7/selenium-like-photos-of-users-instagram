from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from instagramUserInfo import username, password
import time
import argparse
import os
from datetime import datetime



class instagram:
    def __init__(self,username,password):
        self.browserProfile = webdriver.ChromeOptions()
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages':'en,en_US'})
        self.browserProfile.add_argument('--user-agent="Mozilla/5.0 (Windows Phone 10.0; Android 4.2.1; Microsoft; Lumia 640 XL LTE) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Mobile Safari/537.36 Edge/12.10166"')
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.username = username
        self.password = password
    
    def login(self):
        self.browser.get("https://www.instagram.com/accounts/login/")
        time.sleep(1)
        usernameInput =self.browser.find_element_by_name("username")
        passwordInput = self.browser.find_element_by_name("password")
        usernameInput.send_keys(self.username)
        passwordInput.send_keys(self.password)
        passwordInput.send_keys(Keys.ENTER)
        time.sleep(3)
        
    def like(self):
        with open('users.txt', 'r') as f:
            users = f.readlines()
            
        for user in users:
            self.browser.get("https://www.instagram.com/"+user)
            time.sleep(1)
            try:
                photos = self.browser.find_elements_by_css_selector('article a')
                action = webdriver.ActionChains(self.browser)
                time.sleep(0.5)
                photos[0].click()
                time.sleep(1.25)
                like = self.browser.find_element_by_xpath("/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span")
                spanAria = like.get_attribute("aria-label")
                
                if spanAria == 'Like': 
                    time.sleep(1)
                    self.browser.find_element_by_xpath("/html/body/div[3]/div[2]/div/article/div[2]/section[1]/span[1]/button/span").click()
                    time.sleep(0.5)
                    action.send_keys(Keys.ARROW_RIGHT).perform()
                    time.sleep(1)
                    action.send_keys(Keys.ESCAPE).perform()
                else:
                    continue
            except:
                print("continues")
            
        
parser = argparse.ArgumentParser(add_help=True)
parser.add_argument("-u", type=str, help="username")
parser.add_argument("-p", type=str, help="password")
args = parser.parse_args()

insta = instagram(username,password)
insta.login()
insta.like()