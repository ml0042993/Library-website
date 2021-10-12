import pymongo
from random import choice
from Config.Configuration import Parameter
class MongodbClient:
	def __init__(self):
		'''
		初始化
		连接spider数据库
		'''
		self.db = pymongo.MongoClient(Parameter.MONGOCLIENT.value)['spider']

	def add(self,proxy,score=50):
		if len(list(self.db.proxypool.find(proxy).clone())):
			return
		else:
			proxy["Score"] = score
			self.db.proxypool.insert_one(proxy)

	# def keep_sht_CHI(self,message):
	# 	if message['Real_url']:
	# 		tap={}
	# 		tap['Real_url']=message['Real_url']
	# 		if len(list(self.db.shtchi.find(tap).clone())):
	# 			return
	# 		else:
	# 			self.db.shtchi.insert_one(message)
	# 	else:print("无效存储结构")
	def keep_sht(self,json_structure,taps=None):
		if taps == Parameter.SHT_JP.value:
			tap = {}
			tap['Real_url'] = json_structure['Real_url']
			if len(list(self.db.shtjp.find(tap).clone())):
				return
			else:
				return self.db.shtjp.insert_one(json_structure)
		if taps == Parameter.SHT_CHI.value:
			tap = {}
			tap['Real_url'] = json_structure['Real_url']
			if len(list(self.db.shtchi.find(tap).clone())):
				return
			else:
				return self.db.shtchi.insert_one(json_structure)
		# if taps == "":
		# 	return self.db.shtoa.insert_one(json_structure)
	def read_Nosql(self,Nosql_name):
		'''
		:param Nosql_name:需要查询的数据库的名称
		:return: {'Real_url': 'url地址'}
		'''
		# return eval('self.db.{}'.format(Nosql_name)+'.find({},{"Real_url":1,"_id":0})')
		return self.db.get_collection(Nosql_name).find({},{"Real_url":1,"_id":0})
	def keep_sht_core(self,Nosql_name,find_info,update_info):
		# if Nosql_name == 'shtjp':
		# 	return self.db.shtjp.update(find_info,{"$set":update_info})
		# if Nosql_name == 'shtchi':
		# 	return self.db.shtchi.update(find_info,{"$set":update_info})
		# if Nosql_name == 'shtea':
		# 	return self.db.shtea.update(find_info,{"$set":update_info})
		return self.db.get_collection(Nosql_name).update(find_info,{"$set":update_info})

	def max(self,proxy_ip,Max_score = 100):
		'''
		:param proxy_ip: 使用代理的ip作为查询条件
		:param Max_score: 如果能够代理可以连通则设置为100
		:return:
		'''
		print("代理ip为{}，目前可用，设置可用数值为{}".format(proxy_ip,Max_score))

		return self.db.proxypool.update_one({"Ip": proxy_ip}, {"$set": {"Score": Max_score}})

	def decrease(self,proxy_ip,Min_score = 10):
		score = self.db.proxypool.find({"Ip": proxy_ip},{'Score':1,"_id":0})[0]["Score"]

		if score >= Min_score:
			print("代理ip为{}，目前不可用，score数值为{}".format(proxy_ip, score))
			return self.db.proxypool.update_one({"Ip": proxy_ip},{"$inc": {"Score": -10}})
		else:
			print("代理ip为{}，目前不可用，score数值为{},已经移除".format(proxy_ip, score))
			return self.db.proxypool.remove({"Score":{"$lt":10}})


	def random(self):
		proxies_ip=[]
		results = self.db.proxypool.find({"Score":100},{'Ip':1,'Port':1,"_id":0})
		if len(list(results.clone())):
			for result in results:
				ip = result["Ip"]
				port = result["Port"]
				proxy_ip = "http://{}:{}".format(ip,port)
				proxies_ip.append(proxy_ip)
			return choice(proxies_ip)
		else:
			results = self.db.proxypool.find({"Score":{"$gte":10,"$lt":100}},{'Ip':1,'Port':1,"_id":0})
			if len(list(results.clone())):
				for result in results:
					ip = result["Ip"]
					port = result["Port"]
					proxy_ip = "http://{}:{}".format(ip, port)
					proxies_ip.append(proxy_ip)
				return choice(proxies_ip)
			else:
				raise (IndexError,TypeError)

	def count(self):
		return len(list(self.db.proxypool.find({})))

	def all(self):
		'''
		数据量大则使用skip跳过影响性能
		:param sk: 跳过数量
		:param lim: 显示上限
		:return:
		'''
		# result = self.db.proxypool.find({},{'Ip':1,'Port':1,"_id":0}).skip(sk).limit(lim)

		return self.db.proxypool.find({},{'Ip':1,'Port':1,"_id":0})

	def test(self):
		return self.db.get_collection("shtjp").find({},{"Real_url":1,"_id":0})
if __name__ == '__main__':
	obj = MongodbClient()
	for i in obj.test():
		print(i)
	print(obj.test())
	# print(len(list(obj.all().clone())))########
	# taps = math.ceil(len(list(obj.all().clone()))/10)+1
	# for i in range(1,taps):
	# 	sk = 10*i-10
	# 	for j in obj.all().skip(sk).limit(10):
	# 		if j:
	# 			print(j,type(j))
	# 		else:break
	# 	print('\n')