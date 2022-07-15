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

def test_smschk_sendRR(self):
    log = self.getLogger()
    time.sleep(2) ##################Change if page takes time to load#############
    self.driver.find_element(By.XPATH,"//span[normalize-space()='Dashboard']").click()
    time.sleep(4)

    preCustomer = int(self.driver.find_element(By.XPATH,"//body//div//div[@role='tabpanel']//div//div//div[1]//div[2]//span[2]").text)
    precheckin = int(self.driver.find_element(By.XPATH,"//body//div//div[@role='tabpanel']//div//div//div[2]//div[2]//span[2]").text) 
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
    time.sleep(2)
    self.driver.refresh()
    time.sleep(4)

    # sms count check
    smscount_after = int(self.driver.find_element(By.CLASS_NAME , "Sidebar_smsCount__1cD5l").text)
    if smscount == smscount_after - 1:
        log.info("SMS Count reduced by 1 / Working")
    else:
        log.info("SMS count is reducing more than 1")
    self.driver.refresh()
    time.sleep(2)
    self.driver.refresh()
    time.sleep(15)
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



def test_Overview(self):
    log = self.getLogger()
    Overview = int(self.driver.find_element(By.XPATH,"//a[@class='nav-link active']//h6").text)
    Customers = int(self.driver.find_element(By.XPATH,"//a[@data-rb-event-key='Customers']//h6").text)
    PFeedback = int(self.driver.find_element(By.XPATH,"//a[@data-rb-event-key='Feedback']//h6").text)
    Linkclick = int(self.driver.find_element(By.XPATH,"//a[@data-rb-event-key='Link']//h6").text)
    QRscan = int(self.driver.find_element(By.XPATH,"//a[@data-rb-event-key='QR']//h6").text)

    if Overview != 0 and Overview > 0:
        log.info("Overview Count reflecting")
    else:
        log.info("Overview count is not reflecting")

    if Customers != 0 and Customers > 0:
        log.info("Customer Count reflecting")
    else:
        log.info("Customer count is not reflecting")

    if PFeedback !=  0 and PFeedback > 0:
        log.info("PrivateFeedback Count reflecting")
    else:
        log.info("PrivateFeedback count is not reflecting")

    if Linkclick !=0 and Linkclick > 0:
        log.info("Linkclick Count reflecting")
    else:
        log.info("Linkclick count is not reflecting")

    if QRscan !=0 and QRscan > 0:
        log.info("QRscan Count reflecting")
    else:
        log.info("QRscan count is not reflecting")
