import requests
import re
import json
from bs4 import BeautifulSoup

def getHTML(url):
	user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'
	header = {
		'User-Agent' : user_agent	
	}
	try:
		r = requests.get(url)
	except:
		print('get html fail')
		return False
	r.raise_for_status()
	r.encoding = "utf-8"
	return r.text

def is_include_iframe(html):
	soup = BeautifulSoup(html,"html.parser")
	if soup.iframe:
		return 2
	else :
		return 1

def is_include_record(url):
	domain_name = url.split("/")[2] 
	siteLicense = getRecord(domain_name) #获取返回的证书号
	if siteLicense == False : #若此域名没有注册的ICP证书，返回2
		return 2
	re_expression = "ICP"
	compile_ICP = re.compile(re_expression)
	html = getHTML(url)
	soup = BeautifulSoup(html,"html5lib")
	ICPstrings = soup.find_all(string = compile_ICP) #使用正则表达式获取页面的ICP
	print(ICPstrings)
	print(ICPstrings[0][:1])
	number = siteLicense[6:13]
	print(number)
	compile_char = re.compile(siteLicense[:1])
	compile_number = re.compile(number)
	for ICPstring in ICPstrings: #遍历匹配页面获取的ICP信息，
		if compile_char.search(ICPstring) and compile_number.search(ICPstring):
			print("success")
			return 1 #匹配成功，返回1
	return 2 #匹配失败

	# for ICPstring in ICPstrings:

	#soup.prettify()

def getRecord(domain_name):
	user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/12.1.1 Safari/605.1.15'
	header = {
		'User-Agent' : user_agent	
	}
	data = {
		'key' : '061179d47201422e86dfb8ff4fd83a91',
		'domainName' : domain_name
	}#构造请求
	try:
		r = requests.get('http://apidata.chinaz.com/CallAPI/Domain',data=data) #发送请求
	except:
		print("get record fail")
	response = r.json()
	if response['Result'] == None:
		return False
	else :
		SiteLicense = response['Result']['SiteLicense']
		return SiteLicense #返回证书号
	

#def main():
	#print(is_include_record("http://www.jiayuan.edu.cn"))
	#compare_record("www.usc.edu.cn",'')

#main()
