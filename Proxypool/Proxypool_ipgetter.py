from Core.Core_pyquery import Get_pyqueryhtml
class ProxyMetaclass(type):
	def __new__(cls, name, bases,attrs):
		count = 0
		attrs["__FuncName__"]=[]
		for k,v in attrs.items():
			if "__ip_Get" in k:
				attrs["__FuncName__"].append(k)
				count +=1
		attrs["__FunCount__"] = count
		return type.__new__(cls,name,bases,attrs)

class Proxy_Getter(object,metaclass=ProxyMetaclass):
	def __init__(self):
		self.gp = Get_pyqueryhtml()
	def get_proxies(self,callback):
		proxies = []
		for proxy in eval("self.{}()".format(callback)):
			# print("catched succesful")
			proxies.append(proxy)
		return proxies

	# def __ip_Get_jiangxianli(self,pages=4):
	# 	'''
	# 	:return:
	# 	'''
	# 	# proxy = {}#字典不能放到循环外部，会导致在入库时出现id重复的错误，pymongo.errors.DuplicateKeyError:
	# 	home_url = "https://ip.jiangxianli.com/?page={}&anonymity=2"
	# 	urls = [home_url.format(page) for page in range(1,pages+1)]
	# 	for url in urls:
	# 		print("开始获取" + url)
	# 		html = self.gp.Get_html(url)
	# 		if html:
	# 			trs = html('.layui-table tbody tr').items()
	# 			for tr in trs:
	# 				proxy = {}
	# 				proxy['Ip'] = tr.find("td:nth-child(1)").text()
	# 				proxy['Port'] = tr.find("td:nth-child(2)").text()
	# 				proxy['Type'] = tr.find("td:nth-child(3)").text()
	# 				proxy['Link'] = tr.find("td:nth-child(4)").text()
	# 				if len(proxy['Ip']) >= 16:
	# 					continue
	# 				yield proxy
		print('当前网址获取完成')

	# def __ip_Get_66ip(self,pages=10):
	# 	'''
	# 	:return:
	# 	'''
	# 	# proxy = {}#字典不能放到循环外部，会导致在入库时出现id重复的错误，pymongo.errors.DuplicateKeyError:
	# 	home_url = "http://www.66ip.cn/{}.html"
	# 	urls = [home_url.format(page) for page in range(1,pages+1)]
	# 	for url in urls:
	# 		print("开始获取" + url)
	# 		html = self.gp.Get_html(url)
	# 		# print(html)
	# 		if html:
	# 			trs = html('#main table tr').items()
	# 			for tr in trs:
	# 				proxy = {}
	# 				proxy['Ip'] = tr.find("td:nth-child(1)").text()
	# 				proxy['Port'] = tr.find("td:nth-child(2)").text()
	# 				proxy['Type'] = tr.find("td:nth-child(4)").text()
	# 				proxy['Link'] = "HTTP"
	# 				if len(proxy['Ip']) >= 16 or len(proxy['Ip'])<7:
	# 					continue
	# 				yield proxy
	# 	print('当前网址获取完成')

	def __ip_Get_kuaidaili(self, pages=10):
		home_url = "https://www.kuaidaili.com/free/{}/"
		urls = [home_url.format(page) for page in range(1,pages+1)]
		for url in urls:
			print("开始获取" + url)
			html = self.gp.Get_html(url)
			# print(html)
			if html:
				trs = html('.list table tr').items()
				for tr in trs:
					proxy = {}
					proxy['Ip'] = tr.find("td:nth-child(1)").text()
					proxy['Port'] = tr.find("td:nth-child(2)").text()
					proxy['Type'] = tr.find("td:nth-child(3)").text()
					proxy['Link'] = tr.find("td:nth-child(4)").text()
					if len(proxy['Ip']) >= 16 or len(proxy['Ip'])<7:
						continue
					yield proxy
		print('当前网址获取完成')
	def __ip_Get_ihuan(self, pages=None):
		home_url = "https://ip.ihuan.me/?page={}"
		list_page = ['b97827cc','4ce63706','5crfe930','f3k1d581','ce1d45977',]
		urls = [home_url.format(page) for page in list_page]
		for url in urls:
			print("开始获取" + url)
			html = self.gp.Get_html(url)
			# print(html)
			if html:
				trs = html('.table-responsive table tr').items()
				for tr in trs:
					proxy = {}
					proxy['Ip'] = tr.find("td:nth-child(1)").text()
					proxy['Port'] = tr.find("td:nth-child(2)").text()
					proxy['Type'] = tr.find("td:nth-child(7)").text()
					proxy['Link'] = "HTTP"
					if len(proxy['Ip']) >= 16 or len(proxy['Ip'])<7:
						continue
					yield proxy
		print('当前网址获取完成')
	def __ip_Get_7yip(self, pages=10):
		home_url = "https://proxy.ip3366.net/free/?action=china&page={}"
		urls = [home_url.format(page) for page in range(1, pages + 1)]
		for url in urls:
			print("开始获取" + url)
			html = self.gp.Get_html(url)
			# print(html)
			if html:
				trs = html('.container tbody tr').items()
				for tr in trs:
					proxy = {}
					proxy['Ip'] = tr.find("td:nth-child(1)").text()
					proxy['Port'] = tr.find("td:nth-child(2)").text()
					proxy['Type'] = tr.find("td:nth-child(4)").text()
					proxy['Link'] = "HTTP"
					if len(proxy['Ip']) >= 16 or len(proxy['Ip'])<7:
						continue
					yield proxy
		print('当前网址获取完成')
	def __ip_Get_ip3366(self, pages=7):
		home_url = "http://www.ip3366.net/free/?stype=3&page={}"
		urls = [home_url.format(page) for page in range(1, pages + 1)]
		for url in urls:
			print("开始获取" + url)
			html = self.gp.Get_html(url)
			# print(html)
			if html:
				trs = html('#list tbody tr').items()
				for tr in trs:
					proxy = {}
					proxy['Ip'] = tr.find("td:nth-child(1)").text()
					proxy['Port'] = tr.find("td:nth-child(2)").text()
					proxy['Type'] = tr.find("td:nth-child(3)").text()
					proxy['Link'] = "HTTP"
					if len(proxy['Ip']) >= 16 or len(proxy['Ip'])<7:
						continue
					yield proxy
		print('当前网址获取完成')
