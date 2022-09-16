import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import datetime 



#get the current date, month and year.
date = datetime.datetime.now()
current_month = datetime.datetime.strptime(str(date.month), "%m").strftime("%B")
current_year = str(date.year)


#open the webpage
url = "https://www.transport.gov.za/"
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get(url)
driver.implicitly_wait(10)


#click the link
element = driver.find_element(By.LINK_TEXT  , "Fuel rates for the Month of "+current_month+" "+current_year+"").click()


#check link history
