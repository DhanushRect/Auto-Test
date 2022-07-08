import imp
from ipaddress import ip_address
import time
from selenium.webdriver.common.by import By
from utilities.BaseClass import BaseClass
from pageObjects import Dashboard
from pageObjects import Businessprofile
from pageObjects import Inbox
from pageObjects import Customers
from pageObjects import Demo360
from pageObjects import Coupons


class TestOne(BaseClass):


    def test_login(self):
        log = self.getLogger()
        self.driver.find_element(By.ID, "username").send_keys("hurry2dheeraj@gmail.com")
        self.driver.find_element(By.ID, "password").send_keys("9985757091")
        self.driver.find_element(By.XPATH, '//button[text()="Submit "]').click()     
        time.sleep(3) 
        dashboard = "https://app.rectangled.in/dashboard"
        page = self.driver.current_url
        if page == dashboard:
            log.info("Login Successful")
        else:
            log.info("Can't able to login")
            assert page == dashboard


    def test_dashboard(self):
        Dashboard.test_locaion(self)
        Dashboard.test_smschk_sendRR(self)
        Dashboard.test_count(self)

     
    def test_businessprofile(self):
        Businessprofile.test_reviewsystem(self) #Change input details / change location for cleare result


    def test_inbox(self):
        Inbox.test_inboxsearch(self)
        Inbox.test_addcomment(self)
        Inbox.test_addcoupon(self) 


    def test_customers(self):
        Customers.test_customer(self) #Change input details / change location for cleare result


    def test_Demographic(self):
        Demo360.test_Demographic360(self)
    
    
    def test_Coupons(self):
        Coupons.test_Coupon(self) #Chane input details Accordingly to avoid Validation Error


        

      