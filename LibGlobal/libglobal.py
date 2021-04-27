from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
import time
import keyboard

from selenium import webdriver
class Base:
    def browser_launch(self):
        self.driver = webdriver.Chrome(executable_path=r"C:\Users\AIT-LP09\PycharmProjects\Framework\Drivers\chromedriver.exe")
        return self.driver

    def maximize(self):
        self.driver.maximize_window()

    def load_url(self, url):
        self.driver.get(url)

    def page_title(self):
        r = self.driver.title
        return r

    def page_url(self):
        url = self.driver.current_url
        return url

    def fill(self, e, data):
            e.send_keys(data)

    def btn_click(self,element):
        element.click()