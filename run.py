from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Edge()

driver.get('http://piloto.dacclaro.com.pe')

name = driver.find_element(By.NAME, 'loginID')
name.send_keys('D109580')
password = driver.find_element(By.NAME, 'password')
password.send_keys('@GOKU15')
password.submit()
time.sleep(3)
driver.switch_to.frame(0); 
driver.page_source
myLink = driver.find_element(by=By.LINK_TEXT, value='Usuario del canal')
myLink.click()
myLink2 = driver.find_element(by=By.LINK_TEXT, value='Ver jerarquía de usuario')
myLink2.click()
button = driver.find_element(By.NAME, 'submitButton')
button.click()
download = driver.find_element(By.NAME, 'btnSave')
download.click()
##hierarchy = driver.find_element('link text','Ver jerarquía de usuario').click()
##hierarchy.submit()
##submit_name = driver.find_element(By.NAME, 'submitButton').click()
##download_report = driver.find_element(By.NAME, 'btnSave').click()
time.sleep(5)
driver.quit()