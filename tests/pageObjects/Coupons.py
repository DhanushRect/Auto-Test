import time
from selenium.webdriver.common.by import By



def test_Coupon(self):
    log = self.getLogger()
    self.driver.find_element(By.XPATH,"//span[normalize-space()='Coupons']").click()
    self.driver.find_element(By.XPATH,"//button[normalize-space()='Add Coupon']").click()
    self.driver.find_element(By.XPATH,"//input[@id='title']").send_keys("ct5")
    self.driver.find_element(By.XPATH,"//input[@id='active_days']").send_keys("27")
    self.driver.find_element(By.XPATH,"//input[@id='discount_percent']").send_keys("10")
    self.driver.find_element(By.XPATH,"//input[@id='no_of_coupons']").send_keys("10")
    self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(2)
    self.driver.refresh()
    time.sleep(2)
    coupon = self.driver.find_element(By.XPATH,"//tbody/tr[1]/td[2]").text
    if "ct5" == coupon:
        log.info("Coupon Added Successful")
        self.driver.refresh()
        time.sleep(2)
        self.driver.find_element(By.XPATH,"//tbody/tr[1]/td[6]/div[1]/button[1]/i[1]").click()
        self.driver.refresh()
        deleted = self.driver.find_element(By.XPATH,"//tbody/tr[1]/td[1]").text
        time.sleep(2)
        self.driver.refresh()
        if "ct5" == deleted:
            log.info("Coupon Not Deleted / Error")
        else:
            log.info("Coupon Deleted Successful")
    else:
        log.info("Coupon not added")