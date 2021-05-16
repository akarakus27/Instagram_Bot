import time

from selenium import webdriver
from userinfo import username,password
from selenium.webdriver.common.keys import Keys

class Instagram:

    driver_path = "/home/abdulkadir/Masaüstü/git/Instagram_Bot/chromedriver"
    # USERNAME = (By.CLASS_NAME,'username')

    def __init__(self, username, password):
        self.username =username
        self.password =password
        self.browser = webdriver.Chrome(Instagram.driver_path)
        self.browser.maximize_window()

    def signIn(self):
        self.browser.get("https://www.instagram.com/?hl=tr")
        time.sleep(3)
        usernameInput = self.browser.find_element_by_name('username')
        passwordInput = self.browser.find_element_by_name('password')

        usernameInput.send_keys(username)
        passwordInput.send_keys(password)

        passwordInput.send_keys(Keys.ENTER)

        time.sleep(5)
        if self.browser.find_element_by_name('cmbtv'):
            el = self.browser.find_element_by_name('cmbtv')
            el.find_element_by_xpath(".//button[contains(.,'Şimdi Değil')]")

    def getFollowers(self):
        pass

    def followUser(self,username):
        pass

    def unFollowers(self,username):
        pass

    def __del__(self):
        time.sleep(10)
        self.browser.close()

app = Instagram(username,password)

app.signIn()

