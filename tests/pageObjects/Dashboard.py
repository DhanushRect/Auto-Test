import time
from selenium.webdriver.common.by import By


def test_locaion(self):
    # Select Location
    log = self.getLogger()
    self.driver.find_element(By.ID , "dropdown-basic").click()
    time.sleep(2)   
    location = self.driver.find_element(By.XPATH , "(//a[@role='button'])[4]")
    clickedlocation = location.text
    location.click()
    time.sleep(2)
    selectedlocation = self.driver.find_element(By.XPATH , "//span[@class='MasterLocations_locationName__116md']").text
    if selectedlocation == clickedlocation:
        log.info("Location Selected")
    else:
        log.info("Location Not Selected")
    global preCustomer
    global precheckin
    preCustomer = int(self.driver.find_element(By.XPATH,"//body//div//div[@role='tabpanel']//div//div//div[1]//div[2]//span[2]").text)
    precheckin = int(self.driver.find_element(By.XPATH,"//body//div//div[@role='tabpanel']//div//div//div[2]//div[2]//span[2]").text)    

def test_smschk_sendRR(self):
    
    log = self.getLogger()
                       #Review Request 
    smscount = int(self.driver.find_element(By.CLASS_NAME , "Sidebar_smsCount__1cD5l").text)
    if smscount > 0:
        # Send Review request button
        rbutton = self.driver.find_element(By.XPATH, "//button[@class='customPrimary btn btn-primary']")
        rbutton.click()
        # Fill Pop-up and submit
        self.driver.find_element(By.XPATH, "//input[@id='name']").send_keys("TestAuto")
        self.driver.find_element(By.XPATH,"//div[@class='p-0 col-md-4']").click()
        self.driver.find_element(By.XPATH, "//option[@value='+91']").click()
        self.driver.find_element(By.XPATH , "//input[@placeholder='Customer Phone']").send_keys("9398263767")
        self.driver.find_element(By.XPATH, "//button[normalize-space()='Check In']").click()
        log.info("Review Requet Sent")
        time.sleep(2)   
        self.driver.refresh()
    else:
        log.info("SMS Balance is 0")
    self.driver.refresh()
    
    # sms count check
    smscount_after = int(self.driver.find_element(By.CLASS_NAME , "Sidebar_smsCount__1cD5l").text)
    if smscount == smscount_after-1:
        log.info("SMS Count reduced by 1 / Working")
    else:
        log.info("SMS count is reducing more than 1")


def test_count(self):
    log = self.getLogger()
    # customer
    customercount = int(self.driver.find_element(By.XPATH,"//body//div//div[@role='tabpanel']//div//div//div[1]//div[2]//span[2]").text)

    if customercount == preCustomer+1:
        log.info("Customer Count Increases/Working")
    else:
        log.info("Customer count is not increased")

    # checkin
    checkincount = int(self.driver.find_element(By.XPATH,"//body//div//div[@role='tabpanel']//div//div//div[2]//div[2]//span[2]").text)

    if checkincount == precheckin+1:
        log.info("Checkin Count Increases/Working")
    else:
        log.info("Checkin count is not increased")