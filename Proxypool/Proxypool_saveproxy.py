from Proxypool.Proxypool_ipgetter import Proxy_Getter
from Core.Core_Mongodb import MongodbClient
class Getter:
	def __init__(self):
		self.pg = Proxy_Getter()
		self.mc = MongodbClient()
	def run(self):
		for callback_label in range(self.pg.__FunCount__):
			callback = self.pg.__FuncName__[callback_label]
			proxies = self.pg.get_proxies(callback)
			for proxy in proxies:
				self.mc.add(proxy)

if __name__ == '__main__':
	obj = Getter()
	obj.run()