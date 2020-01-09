import DBConncetion
import math
import URLAnomaly
import ContentAnomaly

def countWeight():
	print("countWeight")
	res = DBConncetion.listPhishCharacter() #获取数据库储存的网址特征
	num_list = [[0 for j in range(9)]for j in range(len(res))] #创建一个二维数组
	for i in range(len(res)): 
		for j in range(9):
			min_and_max = DBConncetion.getMaxMinCharacter(str(j+1))
			character_sum = float(DBConncetion.getSumCharacter(str(j+1)))
			character_min = min_and_max['min']
			character_max = min_and_max['max']
			x = (character_max-res[i][j+3])/(character_max-character_min) +character_min #归一化处理
			num_list[i][j] = x/character_sum #计算j项指标下第i个样本值占该指标的比重
	character_weight = [0 for j in range(9)]
	k = 1/(math.log(len(res)))
	for j in range(9):
		sum_p = 0
		for i in range(len(res)):
			sum_p = sum_p + (num_list[i][j] * math.log(num_list[i][j]))
		character_weight[j] = 1-(-(k*sum_p)) #计算信息熵冗余度
	sum_d = 0
	for j in range(9):
		sum_d = sum_d + character_weight[j]
	for j in range(9):
		character_weight[j] = character_weight[j]/sum_d #计算各项指标的权重
	print(character_weight)
	DBConncetion.insertPhishCharacterWeight(character_weight) #向数据库插入此次计算的权重

def countCharacter(url):
	characters = [0 for i in range(10)]
	characters[0] = url
	characters[1] = URLAnomaly.is_include_ip(url)
	characters[2] = URLAnomaly.is_include_at(url)
	characters[3] = URLAnomaly.is_include_port(url)
	characters[4] = URLAnomaly.is_too_deep(url)
	characters[5] = URLAnomaly.is_too_long(url)
	characters[6] = URLAnomaly.is_include_sensitive_word(url)
	characters[7] = URLAnomaly.is_short_link(url)
	characters[8] = ContentAnomaly.is_include_record(url)
	characters[9] = ContentAnomaly.is_include_iframe(url)
	print(characters)
	return characters

def countProbability(characters,character_weight):
	character_weight = DBConncetion.getCharacterWeight()
	logit = character_weight[3]
	for i in range(9):
		logit = logit + characters[i+1]*character_weight[i+3]
	print(logit)
	probability = (math.e**logit)/(1+math.e**logit)
	print(probability)
	characters.append(probability)
	return probability

def isCharacterequality(characters,res):
	for i in range(9):
		if characters[i+1] != res[i+3]:
			return False
	return True

def main():
	url = ""
	characters = countCharacter(url)
	character_weight = DBConncetion.getCharacterWeight() #获取最新权重值
	threshold = character_weight[1]
	probability = countProbability(characters,character_weight) #计算分类概率
	if probability - threshold <= 0:
		print("not phish")
	else :
		print("phish")
	res = DBConncetion.getCharacterByUrl(url) #检查此url是否已经在数据库中
	if res != None:
		if isCharacterequality(characters,res): #判断此链接特征是否与数据库中存储的一致
			if probability != res[-1]:
				DBConncetion.updateProbability([probability,res[0]]) #再判断分类概率是否一致，不一致则更新，因为权重值会改变
		else:
			phish_character = [0 for i in range(11)] #若不一致，则更新特征，并重新计算权重值
			for i in range(9):
				phish_character[i] = characters[i+1]
			phish_character[9] = probability
			phish_character[10] = res[0]
			DBConncetion.updatePhishCharacter(phish_character)
			countWeight()
	else :
		print(characters)
		DBConncetion.insertPhishCharacter(characters) #若数据库中未存储，则插入数据，并重新计算权重值
		countWeight()

main()



