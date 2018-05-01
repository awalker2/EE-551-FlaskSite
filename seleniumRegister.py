#Only one instance allowed to prevent too many requests to stevens site
#https://stackoverflow.com/questions/380870/python-single-instance-of-program
from tendo import singleton
me = singleton.SingleInstance() # will sys.exit(-1) if other instance is running

import sys
import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

#Initial setup, delaying by 10 to obey robots.txt
#None of the accessed URLs paths were prohibited in robots.txt

#One instance reference

#Get the parameters from the user input
username = sys.argv[1] 
password = sys.argv[2] 
call1 = sys.argv[3]
call2 = sys.argv[4]
call3 = sys.argv[5]
call4 = sys.argv[6]
call5 = sys.argv[7]
call6 = sys.argv[8]
call7 = sys.argv[9]
call8 = sys.argv[10]
call9 = sys.argv[11]
call10 = sys.argv[12]
#End of parameters


#Set the delay and open webdriver
delay = 1
driver = webdriver.Chrome()

try:
    #Login user
    driver.get("https://my.stevens.edu/")
    driver.find_element_by_name("j_username").send_keys(username)
    driver.find_element_by_name("j_password").send_keys(password)
    time.sleep(delay)
    driver.find_element_by_name("_eventId_proceed").click()
    #Get on web services portal
    time.sleep(delay)
    driver.get("https://mystevens.stevens.edu/sso/web4student.php")
    #Go to site map
    time.sleep(delay)
    driver.find_element_by_xpath('//*[@title="Site Map"]').click()
    #Go to drop and add classes
    time.sleep(delay)
    driver.find_element_by_link_text('Drop and Add Classes').click()
    #Open the page to add and drop at the top of the hour
    date = datetime.datetime.now()
    secondsLeft = (60 * (60 - date.minute) - date.second)
    time.sleep(secondsLeft)
    driver.find_element_by_name("submitbutton").click()
    #Send the call numbers
    callInput = driver.find_element_by_class_name("dedefaultcenter").find_element_by_name("Callnum")
    callInput.send_keys(call1 + Keys.TAB + call2 + Keys.TAB +call3 + Keys.TAB +call4 + Keys.TAB +call5 +
                    Keys.TAB +call6 + Keys.TAB +call7 + Keys.TAB +call8 + Keys.TAB+call9 + Keys.TAB
                    +call10 + Keys.TAB)
                    #Actually submits it
                    #+Keys.ENTER)
    time.sleep(5)
    driver.close()
except:
    driver.close()
    exit(-1)


    


