from lib2to3.pgen2 import driver
import time
from selenium.webdriver.common.by import By



def test_inboxsearch(self):
    log = self.getLogger()
    self.driver.find_element(By.XPATH,"//span[normalize-space()='Inbox']").click()
    self.driver.find_element(By.XPATH,"//span[normalize-space()='Private Feedback']").click()
    time.sleep(2)
    self.driver.find_element(By.XPATH,"//input[@id='search-bar-0']").send_keys("Dhanush")
    time.sleep(2)
    value = self.driver.find_element(By.CSS_SELECTOR,"tbody tr:nth-child(1) td:nth-child(2)").text
    if value == "Dhanush":
        log.info("Inbox search is working")
    else:
        log.info("Inbox search is not working")
def test_addcomment(self):
    log = self.getLogger()
    self.driver.find_element(By.XPATH,"//span[normalize-space()='Inbox']").click()
    self.driver.find_element(By.XPATH,"//span[normalize-space()='Private Feedback']").click()
    self.driver.find_element(By.XPATH,"//tbody/tr[1]/td[9]/div[1]/button[1]/i[1]").click()
    self.driver.find_element(By.XPATH,"//input[@id='name']").send_keys("Add comment")
    self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
    time.sleep(2)
    self.driver.implicitly_wait(4)
    comment = self.driver.find_element(By.XPATH,"//div[@class='list-group-item']//div//b").text
    if comment == "Add comment":
        log.info("Comment Added")
        self.driver.refresh()
    else:
        log.info("Comment not Added")


def test_addcoupon(self):
    log = self.getLogger()
    # add coupon
    self.driver.find_element(By.XPATH,"//tbody/tr[1]/td[9]/div[1]/button[2]/i[1]").click()
    self.driver.find_element(By.XPATH,"//select[@id='coupon_id']").click()
    self.driver.find_element(By.XPATH,"//option[@value='65']").click()
    self.driver.find_element(By.XPATH,"//select[@id='code']").click()
    self.driver.find_element(By.XPATH,"//div[@coupons='[object Object],[object Object],[object Object]']//div//div//div[2]//select[1]//option[2]").click()
    self.driver.find_element(By.XPATH,"//input[@placeholder='Enter Comments']").send_keys("Another Comment")
    self.driver.find_element(By.XPATH,"//button[@type='submit']").click()
    self.driver.refresh()
    self.driver.implicitly_wait(2)
    self.driver.find_element(By.XPATH,"//body[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[2]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[9]/div[1]/button[1]").click()
    couponmessage = self.driver.find_element(By.XPATH,"//body/div[@role='dialog']/div[@commentdata='[object Object]']/div/div/div/div[1]/div[1]/b[1]").text
    print(couponmessage)
    self.driver.implicitly_wait(5)
    self.driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
    self.driver.refresh()
    if 1 == 1 :
       assert "Coupon alloted:" in couponmessage
       print("Coupon Added")
    else:
        assert "Coupon alloted:" in couponmessage
        print("Coupon Not Added")


