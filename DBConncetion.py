import pymysql
import math
from decimal import Decimal
def insertPhish(url):
	host = "localhost"
	user = "root"
	passwd = "jiayuandemysql"
	conn = pymysql.connect(host,user,passwd)
	conn.select_db('phish_detection')
	cur = conn.cursor()
	sql = "insert into phish_web(phish_url) values (%s)"
	cur.execute(sql,url)
	cur.close()
	conn.commit()
	conn.close()
	print("insert success")

def listPhish():
	host = "localhost"
	user = "root"
	passwd = "jiayuandemysql"
	conn = pymysql.connect(host,user,passwd)
	conn.select_db('phish_detection')
	cur = conn.cursor()
	cur.execute("select * from phish_web")
	response = []
	while 1:
		res = cur.fetchone()
		if res is None:
			break
		response.append(res)
		print(res)
	cur.close()
	conn.commit()
	conn.close()
	return response

def findphishUrl(url):
	host = "localhost"
	user = "root"
	passwd = "jiayuandemysql"
	conn = pymysql.connect(host,user,passwd)
	conn.select_db('phish_detection')
	cur = conn.cursor()
	sql = "select * from phish_web where phish_url= %s"
	cur.execute(sql,url)
	res = cur.fetchone()
	if res is None:
		return False
	cur.close()
	conn.commit()
	conn.close()
	return True


def insertPhishCharacter(characters):
	host = "localhost"
	user = "root"
	passwd = "jiayuandemysql"
	conn = pymysql.connect(host,user,passwd)
	conn.select_db('phish_detection')
	cur = conn.cursor()
	sql = "insert into phish_character(phish_url,character1,character2,character3,character4,character5,character6,character7,character8,character9,probability) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	cur.execute(sql,characters)
	cur.close()
	conn.commit()
	conn.close()
	print("insert success")

def insertPhishCharacterWeight(character_weights):
	host = "localhost"
	user = "root"
	passwd = "jiayuandemysql"
	conn = pymysql.connect(host,user,passwd)
	conn.select_db('phish_detection')
	cur = conn.cursor()
	sql = "insert into phish_character_weight(character_weight1,character_weight2,character_weight3,character_weight4,character_weight5,character_weight6,character_weight7,character_weight8,character_weight9) values (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	print(character_weights)
	cur.execute(sql,character_weights)
	cur.close()
	conn.commit()
	conn.close()
	print("insert success")

def listPhishCharacter():
	host = "localhost"
	user = "root"
	passwd = "jiayuandemysql"
	conn = pymysql.connect(host,user,passwd)
	conn.select_db('phish_detection')
	cur = conn.cursor()
	sql = "select * from phish_character"
	cur.execute(sql)
	res = cur.fetchall()
	cur.close()
	conn.commit()
	conn.close()
	return res

def getMaxMinCharacter(number):
	host = "localhost"
	user = "root"
	passwd = "jiayuandemysql"
	conn = pymysql.connect(host,user,passwd)
	conn.select_db('phish_detection')
	cur = conn.cursor()
	character_string = 'character' + number
	sql = "select max("+character_string+") from phish_character"
	cur.execute(sql)
	res = cur.fetchone()
	maxCharacter = res[0]
	sql = "select min("+character_string+") from phish_character"
	cur.execute(sql)
	res = cur.fetchone()
	minCharacter = res[0]
	cur.close()
	conn.commit()
	conn.close()
	maxMinCharacter = {'min':minCharacter,'max':maxCharacter}
	return maxMinCharacter

def getSumCharacter(number):
	host = "localhost"
	user = "root"
	passwd = "jiayuandemysql"
	conn = pymysql.connect(host,user,passwd)
	conn.select_db('phish_detection')
	cur = conn.cursor()
	character_string = 'character' + number
	sql = "select sum("+character_string+") from phish_character"
	cur.execute(sql)
	res = cur.fetchone()
	sumCharacter = res[0]
	cur.close()
	conn.commit()
	conn.close()
	print('sum: '+str(res[0]))
	return sumCharacter

def getCharacterWeight():
	host = "localhost"
	user = "root"
	passwd = "jiayuandemysql"
	conn = pymysql.connect(host,user,passwd)
	conn.select_db('phish_detection')
	cur = conn.cursor()
	sql = "select * from phish_character_weight where id = (select max(id) from phish_character_weight)"
	cur.execute(sql)
	res = cur.fetchone()
	print(res)
	cur.close()
	conn.commit()
	conn.close()
	print('max: '+str(res[0]))
	return res

def getCharacterByUrl(url):
	host = "localhost"
	user = "root"
	passwd = "jiayuandemysql"
	conn = pymysql.connect(host,user,passwd)
	conn.select_db('phish_detection')
	cur = conn.cursor()
	sql = "select * from phish_character where phish_url = %s"
	cur.execute(sql,url)
	res = cur.fetchone()
	print(res)
	cur.close()
	conn.commit()
	conn.close()
	return res

def updateProbability(probability):
	host = "localhost"
	user = "root"
	passwd = "jiayuandemysql"
	conn = pymysql.connect(host,user,passwd)
	conn.select_db('phish_detection')
	cur = conn.cursor()
	sql = "update phish_character set probability = %s where phish_id = %s"
	cur.execute(sql,probability)
	cur.close()
	conn.commit()
	conn.close()

def updatePhishCharacter(phish_character):
	host = "localhost"
	user = "root"
	passwd = "jiayuandemysql"
	conn = pymysql.connect(host,user,passwd)
	conn.select_db('phish_detection')
	cur = conn.cursor()
	sql = "update phish_character set character1,character2,character3,character4,character5,character6,character7,character8,character9,probability = %s,%s,%s,%s,%s,%s,%s,%s,%s,%s where phish_id = %s"
	cur.execute(sql,phish_character)
	cur.close()
	conn.commit()
	conn.close()

def listPhishCharacter():
	host = "localhost"
	user = "root"
	passwd = "jiayuandemysql"
	conn = pymysql.connect(host,user,passwd)
	conn.select_db('phish_detection')
	cur = conn.cursor()
	sql = "select * from phish_character where is_phish = 1"
	cur.execute(sql)
	res = cur.fetchall()
	cur.close()
	conn.commit()
	conn.close()
	return res





