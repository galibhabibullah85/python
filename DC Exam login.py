from selenium import webdriver
from selenium.webdriver.common.by import By

url = "http://qb.eshiksabd.com/Question-Bank-Center"
browser = webdriver.Firefox()
browser.get(url)

anchors = browser.find_element_by_class_name('signinButton')
usrFld = browser.find_element_by_id('inputtext')
pwdFld = browser.find_element_by_id('inputPassword')
usrFld.send_keys("1202021010431") #send_keys() inserts text into input/textarea tag
pwdFld.send_keys("3949040431")
anchors.click()

btn = browser.find_element_by_id('startExam')
btn.click()