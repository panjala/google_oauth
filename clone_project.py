import socket
import os
import time, datetime, os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

path="/home/sai/Documents/POF"
today = datetime.date.today()  
os.chdir(path)
if os.path.exists(today.strftime("%Y-%m-%d")):
    print "project avaliable in folder"
else:
    folder=os.makedirs(today.strftime("%Y-%m-%d"))
    res=os.getcwd()
    des= res+'/'+ today.strftime("%Y-%m-%d")
    cmd = "scp -r -P 9001 phoneofriend@196.12.47.68:/home/phoneofriend/New_Oscar/django-oscar /des"
    os.system(cmd)
'''browser = webdriver.Firefox()
browser.get('http://gmail.com')
action = webdriver.ActionChains(browser)
emailElem = browser.find_element_by_id('Email')
emailElem.send_keys('spanjala87@gmail.com')
nextButton = browser.find_element_by_id('next')
nextButton.click()
time.sleep(1)
passwordElem = browser.find_element_by_id('Passwd')
passwordElem.send_keys('Qualcomm2')
signinButton = browser.find_element_by_id('signIn')
signinButton.click()'''
