from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

callNums = ["123", "123", "123"]


driver = webdriver.Chrome()

driver.get("https://my.stevens.edu/")
driver.find_element_by_name("j_username").send_keys("awalker2")
driver.find_element_by_name("j_password").send_keys("pass")
driver.find_element_by_name("_eventId_proceed").click()

driver.get("https://mystevens.stevens.edu/sso/web4student.php")
driver.find_element_by_xpath('//*[@title="Site Map"]').click()
driver.find_element_by_link_text('Drop and Add Classes').click()
driver.find_element_by_name("submitbutton").click()

callInput = driver.find_element_by_class_name("dedefaultcenter").find_element_by_name("Callnum")
callInput.send_keys(callNums[0] + Keys.TAB + callNums[1] + Keys.TAB + callNums[2] + Keys.TAB)
    
time.sleep(5)
driver.close()
