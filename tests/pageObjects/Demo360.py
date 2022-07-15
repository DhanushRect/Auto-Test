import time
from selenium.webdriver.common.by import By



def test_Demographic360(self):
    log = self.getLogger()
    self.driver.find_element(By.XPATH,"//span[normalize-space()='Demographic 360°']").click()
    # top cities
    self.driver.implicitly_wait(5)
    tc1 = (self.driver.find_element(By.XPATH,"//body[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[1]/td[2]/div[1]/span[1]").text)
    tc2 = (self.driver.find_element(By.XPATH,"//body[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[2]/td[2]/div[1]/span[1]").text)
    tc3 = (self.driver.find_element(By.XPATH,"//body[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[3]/td[2]/div[1]/span[1]").text)
    tc4 = (self.driver.find_element(By.XPATH,"//body[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[4]/td[2]/div[1]/span[1]").text)
    tc5 = (self.driver.find_element(By.XPATH,"//body[1]/div[1]/section[1]/div[1]/div[1]/div[2]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/div[1]/table[1]/tbody[1]/tr[5]/td[2]/div[1]/span[1]").text)
    if tc1 != 0:
        log.info("Demographic360 - Top 5 Cities Working")
    elif tc3 !=0:
        log.info("Demographic360 - Top 5 Cities Working")
    else:
        log.info("Not Working")
    # interest
    ti1 = (self.driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(1) > td:nth-child(2) > div:nth-child(1) > span:nth-child(1)").text)
    ti2 = (self.driver.find_element( By.CSS_SELECTOR,"body > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(2) > td:nth-child(2) > div:nth-child(1) > span:nth-child(1)").text)
    ti3 = (self.driver.find_element( By.CSS_SELECTOR,"body > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(3) > td:nth-child(2) > div:nth-child(1) > span:nth-child(1)").text)
    ti4 = (self.driver.find_element( By.CSS_SELECTOR,"body > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(4) > td:nth-child(2) > div:nth-child(1) > span:nth-child(1)").text)
    ti5 = (self.driver.find_element( By.CSS_SELECTOR,"body > div:nth-child(1) > section:nth-child(1) > div:nth-child(2) > div:nth-child(2) > div:nth-child(2) > div:nth-child(1) > div:nth-child(4) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > table:nth-child(1) > tbody:nth-child(2) > tr:nth-child(5) > td:nth-child(2) > div:nth-child(1) > span:nth-child(1)").text)

    if ti1 !=0:
        log.info("Demographic360 - Top 5 Interest Working")
    elif ti3 !=0:
        log.info("Demographic360 - Top 5 Interest Working")
    else:
        log.info("Not Working")
    self.driver.find_element(By.XPATH,"//img[@alt='logo']").click()
