    # Importing libraries
import time
import requests
import hashlib
from urllib.request import urlopen, Request
import datetime
import errno
import os
from pathlib import Path
import tkinter
from tkinter import *
from tkinter import messagebox
import os
from time import sleep
import smtplib
from email.mime.text import MIMEText
import validators
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import codecs
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from bs4 import BeautifulSoup
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

window = tkinter.Tk()
window.title("Department of transport SA")
window.geometry('500x300')
img = PhotoImage(file=r"L:\Nteboheng\img\Trans.png")
label = Label(
    window,
    image=img
)
label.place(x=0, y=0)
#file_path ="https://dms.dot.gov.za/share/s/RfqaojggTHOm2nuNZFTcfw"
file_path ="https://dms.dot.gov.za/share/s/HBN-cWC-SPm9xpJqArSfOQ"
# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
def fileInfor():
    global file_path
    global path_change
    username = os.getlogin()
    user = r'C:\Users\''
    user_remove = user[:-1]
    loc = '\SANSA\Space Operations Reception - Documents\FUEL TARIFFS\''
    lol_remove = loc[:-1]
    string = '\\'
    l = '2022'
    #get the month and year of todays date
    datetime_today  = datetime.datetime.now()
    dmy_tostring = datetime_today.strftime('%B%Y')
    dy_tostring = datetime_today.strftime('%Y')
    datetime_month_year = datetime.datetime.strptime(dmy_tostring , '%B%Y')

    path_to_file = user_remove + username + lol_remove +string+dy_tostring+string

    chrome_drive = user_remove + username + '\Documents\chromedriver'



    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    download_location = {"download.default_directory": path_to_file}
    options.add_experimental_option("prefs",download_location)

    #Locate the chomedriver that supports google vers
    chrome_driver_path = Service(chrome_drive)
    browser = webdriver.Chrome(service = chrome_driver_path, options =options )

    browser.get(file_path)

    get_url = browser.current_url
    path_web = Path(file_path)
    wait = WebDriverWait(browser ,604800)
    wait.until(EC.url_changes(get_url))

    #Validate if url is valid
    valid=validators.url(file_path)
    key_to_file_exists = 'download.default_directory'


    try :
            sleep(2)
            btn_download = browser.find_element(By.ID, "page_x002e_components_x002e_quickshare_x0023_web-preview-download-button")
            btn_download.click()

            btn_original = browser.find_element(By.CLASS_NAME,  "yuimenuitemlabel")
            btn_original.click()
            sleep(2)
            file_path = browser.current_url
            print(file_path)
            bottom_frame = tkinter.Frame(window).pack(side = "bottom")
            btn = tkinter.Label(bottom_frame, text = "File Saved ", bg = "green").pack(side = "bottom") #'side' is used to left or right align the widgets

            try:
                #Create your SMTP session
                smtp = smtplib.SMTP('smtp.office365.com', 587)

                   #Use TLS to add security
                smtp.starttls()

                    #User Authentication
                

                    #Defining The Message
                message_hour = MIMEText("\n File for  " +  dmy_tostring +  " is downloaded and storred on SANSA DRIVE. ")
                recipients = ['nmolefe@sansa.org.za']
                message_hour['Subject'] = "FUEL TARIFFS"
                sender = 'automation@sansa.org.za'
                message_hour['From'] = sender
                message_hour['To'] = ", ".join(recipients)
                    #Sending the Email
                smtp.sendmail(sender, recipients,message_hour.as_string())

                    #Terminating the session
                smtp.quit()

            except Exception as ex:
                messagebox.showinfo("Something went wrong....",ex)

            os.system("taskill /m Fuel_Tariffs.py")
    except Exception as ex:
        messagebox.showinfo("The url change detected is not valid ....")
        bottom_frame = tkinter.Frame(window).pack(side = "bottom")
        btn = tkinter.Label(bottom_frame, text = "An error occured!", bg = "red").pack(side = "bottom") #'side' is used to left or right align the widgets
        pass


while True:
  fileInfor()
  break
window.mainloop()