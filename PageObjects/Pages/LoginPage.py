from selenium.webdriver.common.by import By

from PageObjects import Locators


class LoginPage:
    def __init__(self,driver):
        self.txt_username = driver.find_element(By.NAME, Locators.username_id)
        self.txt_pass = driver.find_element(By.NAME, Locators.password_id)
        self.clk_login = driver.find_element(By.NAME, Locators.press_login_name)

    #getters
    def getTxtUserName(self):
        return self.txt_username

    def getTxtPass(self):
        return self.txt_pass

    def getClkLogin(self):
        return self.clk_login
