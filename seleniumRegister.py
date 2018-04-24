from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
<<<<<<< HEAD

#Initial setup, delaying by 10 to obey robots.txt
#None of the accessed URLs paths were prohibited in robots.txt

def automatedRegister(user, password, call1="",call1=2="",call3="",call4="",call5="",call6="",call7="",call8=""):
    delay = 10
    driver = webdriver.Chrome()

    driver.get("https://my.stevens.edu/")
    driver.find_element_by_name("j_username").send_keys(user)
    driver.find_element_by_name("j_password").send_keys(password)

    time.sleep(delay)
    driver.find_element_by_name("_eventId_proceed").click()

    time.sleep(delay)
    driver.get("https://mystevens.stevens.edu/sso/web4student.php")

    time.sleep(delay)
    driver.find_element_by_xpath('//*[@title="Site Map"]').click()

    time.sleep(delay)
    driver.find_element_by_link_text('Drop and Add Classes').click()

    time.sleep(delay)
    driver.find_element_by_name("submitbutton").click()

    time.sleep(delay)
    callInput = driver.find_element_by_class_name("dedefaultcenter").find_element_by_name("Callnum")
    callInput.send_keys(call1 + Keys.TAB + call2 + Keys.TAB +call3 + Keys.TAB +call4 + Keys.TAB +call5 +
                        Keys.TAB +call6 + Keys.TAB +call7 + Keys.TAB +call8 + Keys.TAB)
        
    time.sleep(5)
    driver.close()
=======
>>>>>>> a8c595c0ed4785e1ae91ea33387135f361111a15
