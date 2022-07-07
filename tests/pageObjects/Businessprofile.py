import time
from selenium.webdriver.common.by import By



def test_reviewsystem(self):
    log = self.getLogger()
    self.driver.find_element(By.XPATH,"//span[normalize-space()='Business Profile']").click()
    time.sleep(2)
    self.driver.find_element(By.XPATH,"//div[@class='card-body']//a[@class='customPrimary innerTabButton btn btn-primary']").click()
    windows = self.driver.window_handles
    self.driver.switch_to.window(windows[1])
    time.sleep(2)
    
    oldreview = "button-container"
    reviewpage = self.driver.find_element(By.XPATH,"//body/div/div[3]").get_attribute("class")
    def review_collection():
        self.driver.find_element(By.XPATH,"//a[normalize-space()='I did not like it!']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,"//div[@class='starrr']//a[position()=4]").click()
        self.driver.find_element(By.XPATH,"//input[@placeholder='Name*']").send_keys("checkold10")
        self.driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("9398263767")
        self.driver.find_element(By.XPATH,"//textarea[@placeholder='How can we improve?']").send_keys("auto_improve")
        self.driver.find_element(By.XPATH,"//button[@id='submit-fb']").click()
        self.driver.close()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[0])
        self.driver.find_element(By.XPATH,"//span[normalize-space()='Inbox']").click()
        self.driver.find_element(By.XPATH,"//span[normalize-space()='Private Feedback']").click()
        time.sleep(2)
        value = self.driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(1) td:nth-child(2)").text
        oldpage = "checkold10"
        if oldpage == value:
            log.info("old Reviwe Page Working and Collecting data")
            log.info("Private Feedback is working and getting data")
        else:
            log.info("old Reviwe Page is not Working and Collecting data")
            log.info("Private Feedback is not working and getting data")
        self.driver.find_element(By.XPATH,"//span[normalize-space()='Business Profile']").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,"//div[@class='ProfileSettings_pageSettings__1qpQr']//span[contains(text(),'Edit')]").click()
        self.driver.find_element(By.XPATH,"//label[@for='smartReview']//span[@class='slider round']").click()
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-outline-primary']").click()
        self.driver.refresh()
        self.driver.find_element(By.XPATH,"//div[@class='card-body']//a[@class='customPrimary innerTabButton btn btn-primary']").click()
        time.sleep(2)
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//body/div/div/div/div/a[2]").click()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,"//input[@placeholder='Name*']").send_keys("checknew10")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//input[@id='phone']").send_keys("9398263767")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div[@class='tags-container']//span[2]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//div[@class='bootstrap-tagsinput']//input[@type='text']").send_keys("auto_improve_2")
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[@id='submit-fb']").click()
        time.sleep(2)
        self.driver.close()
        self.driver.switch_to.window(windows[0])
        self.driver.find_element(By.XPATH,"//span[normalize-space()='Inbox']").click()
        self.driver.find_element(By.XPATH,"//span[normalize-space()='Private Feedback']").click()
        time.sleep(2)
        value = self.driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(1) td:nth-child(2)").text
        newpage = "checknew10"
        if newpage == value:
            log.info("Smart Reviwe Page Working and Collecting data")
            log.info("Private Feedback is working and getting data for Smart-Review")
        else:
            log.info("Smart Reviwe Page is not Working and Collecting data")
            log.info("Private Feedback is not working and getting data for Smart-Review")
    
    if oldreview == reviewpage:
        review_collection()
    elif oldreview != reviewpage:
        self.driver.close()
        self.driver.switch_to.window(windows[0])
        self.driver.refresh()
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.XPATH,"//div[@class='ProfileSettings_pageSettings__1qpQr']//span[contains(text(),'Edit')]").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//label[@for='smartReview']//span[@class='slider round']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//button[@class='btn btn-outline-primary']").click()
        time.sleep(2)
        self.driver.refresh()
        self.driver.find_element(By.XPATH,"//div[@class='card-body']//a[@class='customPrimary innerTabButton btn btn-primary']").click()
        windows = self.driver.window_handles
        self.driver.switch_to.window(windows[1])
        time.sleep(2)
        review_collection()
    else:
        log.info("Preview Not working")
    



