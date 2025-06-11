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

        time.sleep(2)
        if self.browser.find_element_by_class_name('cmbtv'):
            el = self.browser.find_element_by_class_name('cmbtv')
            el.find_element_by_xpath(".//button[contains(.,'Şimdi Değil')]")

    def getFollowers(self):
        self.browser.get(f"https://www.instagram.com/{self.username}")
        time.sleep(2)
        self.browser.find_element_by_class_name("k9GMp").find_element_by_tag_name("a").click()
        time.sleep(2)
        followers = self.browser.find_element_by_class_name("PZuss").find_elements_by_tag_name("li")
        for user in followers:
            link = user.find_element_by_tag_name("a").get_attribute("href")
            print(link)


    def followUser(self,username):
        self.browser.get(f"https://www.instagram.com/{username}/")
        time.sleep(2)
        follow_button = self.browser.find_element_by_tag_name("button")
        button_text = follow_button.text.lower()
        if button_text == "takip et" or button_text == "follow":
            follow_button.click()

    def unFollowers(self,username):
        self.browser.get(f"https://www.instagram.com/{username}/")
        time.sleep(2)
        follow_button = self.browser.find_element_by_tag_name("button")
        button_text = follow_button.text.lower()
        if button_text == "takiptesin" or button_text == "following":
            follow_button.click()
            time.sleep(1)
            self.browser.find_element_by_xpath("//button[contains(text(), 'unfollow')]" \
                "| //button[contains(text(), 'Takibi bırak')]").click()

    def __del__(self):
        time.sleep(10)
        self.browser.close()

app = Instagram(username,password)

app.signIn()
app.getFollowers()

