import re
def is_include_ip(url):
	re_expression = "(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|[1-9])\.((1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)\.){2}(1\d{2}|2[0-4]\d|25[0-5]|[1-9]\d|\d)"
	compile_ip = re.compile(re_expression)
	if compile_ip.search(url):
		return 2
	else :
		return 1

def is_include_at(url):
	re_expression = "@"
	compile_at = re.compile(re_expression)
	if compile_at.search(url):
		return 2
	else :
		return 1

def is_include_port(url):
	re_expression = ":((\d)|(\d{2})|(\d{3})|(\d{4})|(\d{5}))"
	compile_port = re.compile(re_expression)
	if compile_port.search(url):
		return 2
	else :
		return 1

def is_too_deep(url):
	count = 0
	domain_name = url.split("/")[2]
	for domain_name_char in domain_name:
		if domain_name_char == '.':
			count+=1
	if count > 3 :
		return 2
	else :
		return 1

def is_too_long(url):
	if len(url) > 23:
		return 2
	else :
		return 1

def is_short_link(url):
	re_expression = "(sina.lt)|(t.cn)|(dwz.cn)|(goo.gl)|(bit.ly)|(qq.cn.hn)|(tb.cn.hn)|(jd.cn.hn)|(j.mp)"
	compile_shortlink = re.compile(re_expression)
	if compile_shortlink.search(url):
		return 2
	else :
		return 1

def is_include_sensitive_word(url):
	re_expression = "(account)|(login)|(alibaba)|(taobao)|(paypal)|(alipay)|(ebay)|(amazon)|(bank)|(jd)|(icbc)|(apk)|(mobile)|(webapp)"
	compile_sensitive_word = re.compile(re_expression)
	if compile_sensitive_word.search(url):
		return 2
	else :
		return 1
