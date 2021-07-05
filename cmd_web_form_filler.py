from bs4 import BeautifulSoup as soup
import requests

url = 'https://bdcmoney.com/Log_in/'
response = requests.get(url)
html_content = response.text

html_soup = soup(html_content,'html.parser')
inputs = html_soup.find_all('input')
# print(inputs)

# for inp in inputs:
# 	print(soup.prettify(inp))
email = input('Enter your email-address: ')
pwd = input('Enter your password: ')

data = {
	'email':email,
	'pwd':pwd,
	'log_in':'Log-in',
}

response = requests.post(url,data=data)
response_html = soup(response.text,'html.parser')
alerts = response_html.find_all('script')
print(soup.prettify(alerts[0]))
# print(type(alerts[0]))
print(dir(alerts[0]))
print(alerts[0].get_text('alert'))

if 'alert' in alerts[0]:
	print("______________________________________")
	print("Credentials did not matched!")
	print("______________________________________")
else:
	print("______________________________________")
	print("Credentials matched!")
	print("______________________________________")