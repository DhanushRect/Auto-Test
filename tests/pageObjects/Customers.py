from lib2to3.pgen2 import driver
import time
from selenium.webdriver.common.by import By


def test_customersearch(self):
    log = self.getLogger()
    self.driver.find_element(By.XPATH,"//span[normalize-space()='Customers']").click()
    self.driver.implicitly_wait(5)
    self.driver.find_element(By.XPATH,"//input[@id='search-bar-0']").send_keys("Dhanush")
    time.sleep(3)
    srtxt = self.driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(1) td:nth-child(1)").text
    
    if srtxt == "Dhanush":
        log.info("Customer Search is Working")
    else:
        log.info("Customer Search is Working")



def test_customer(self):
    log = self.getLogger()
    self.driver.implicitly_wait(5)
    self.driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(1) > section:nth-child(1) > aside:nth-child(1) > ul:nth-child(3) > li:nth-child(5) > a:nth-child(1) > span:nth-child(2)").click()
    self.driver.find_element(By.XPATH, "//button[@class='customPrimary btn btn-primary']").click()
    self.driver.find_element(By.XPATH, "//input[@id='name']").send_keys("Automate1")
    self.driver.find_element(By.XPATH,"//div[@class='p-0 col-md-4']").click()
    self.driver.find_element(By.XPATH, "//option[@value='+91']").click()
    self.driver.find_element(By.XPATH , "//input[@placeholder='Customer Phone']").send_keys("9398263767")
    self.driver.find_element(By.XPATH, "//button[normalize-space()='Check In']").click()
    time.sleep(1)
    self.driver.refresh()
    time.sleep(3)
    self.driver.implicitly_wait(5)
    name = self.driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(1) td:nth-child(1)").text
    if name == "Automate1":
        log.info("Customer data is storinig")
    else:
        log.info("Customer data is not storing")
    self.driver.refresh()
    time.sleep(2)
    self.driver.find_element(By.XPATH,"//button[normalize-space()='Add Customer']").click()
    self.driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Addcheck1")
    self.driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("9398263767")
    self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(2)
    name2 = self.driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(1) td:nth-child(1)").text
    if name2 == "Addcheck1":
        log.info("Customer added")
    else:
        log.info("Customer Not Added")
    self.driver.refresh()