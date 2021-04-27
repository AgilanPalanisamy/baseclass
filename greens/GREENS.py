import time
from selenium.webdriver.common.by import By

from LibGlobal.libglobal import * # instead of base we are using *
from PageObjects.Pages.LoginPage import LoginPage


class Company(Base):
    def login(self):
        # b = Base()
        driver = self.browser_launch()
        self.maximize()
        self.load_url("http://adactin.com/HotelApp/")
        print(self.page_title())
        print(self.page_url())
        l = LoginPage(driver)
        self.fill(l.getTxtUserName(),"Pavithrakumar")
        time.sleep(2)
        self.fill(l.getTxtPass(),"")
        time.sleep(3)
        self.btn_click(l.getClkLogin())




c = Company()
c.login()