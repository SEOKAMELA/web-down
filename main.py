import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import datetime
from time import sleep




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

#switch tab and download 
driver.switch_to.window(driver.window_handles[1])
download_one = driver.find_element(By.ID, "page_x002e_components_x002e_quickshare_x0023_web-preview-download-button").click() #lets hope their id wont change
download_original = driver.find_element(By.LINK_TEXT, "Download Original").click()

sleep(2)
