"""--------------Importing all the stufs---------------"""
import pyexcel as pe
from getmac import get_mac_address as gma
from selenium import webdriver
import time



"""--------------Checking the mac-address---------------"""
realmac = gma()
usrmac = "14:da:e9:18:b6:18"#-------------Need to define buyer's mac-address here--------------------------------
if realmac != usrmac:
	exit()

print(end='\n')
print("==========>Don't do anything while running the process<==========")

"""-----------------Main functions----------------------"""
url = "https://quickemailverification.com/"
browser = webdriver.Firefox()
browser.get(url)



"""----------------Login process---------------------"""
browser.find_element_by_link_text('Login').click()
while True:
	try:
		browser.find_element_by_id("email").send_keys("ahmostofa089@gmail.com")
		browser.find_element_by_id("password").send_keys("P@ssw0rd12345678910")
		browser.find_element_by_id('login').click()
		break
	except:
		continue


xls_file = pe.iget_records(file_name='leads.xls')
xls_file_sheet = pe.get_sheet(file_name='leads.xls')
xls_file_sheet.column += ['']
xls_file_sheet.column += ['']
xls_file_sheet.column += ['Status']
status_record = ['Status']




"""---------------Function for recursion-----------------"""
def proceed(data,st):
	"""-------------Email inputting & verify_click---------"""
	while True:
		try:
			browser.find_element_by_id("email").send_keys(data['E-mail'])
			browser.find_element_by_id('verify').click()
			break
		except:
			continue


	"""--------------Getting the status---------------------"""
	while True:
		try:
			# status = browser.find_element_by_class_name('col-sm-12')
			status = browser.find_element_by_xpath('/html/body/div[1]/div[3]/div[10]/div/div/div[2]/div[1]/div/div')
			status_text = status.get_attribute('innerText')
			st.append(status_text)
			break
		except:
			continue



	while True:
		try:
			browser.find_element_by_class_name('close').click()
			break
		except:
			continue


for record in xls_file:
	time.sleep(1)
	proceed(record,status_record)

	

#---------Importimg status into the file------------
	xls_file_sheet.column[3] = status_record
	xls_file_sheet.save_as('leads.xls')



print("==========>Process completed success fully<==========")
browser.quit()
exit()