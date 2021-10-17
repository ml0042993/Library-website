from Proxypool.Proxypool_ipgetter import Proxy_Getter
from Core.Core_Mongodb import MongodbClient
from threading import Thread
class Getter:
	def __init__(self,set_name):
		self.pg = Proxy_Getter()
		self.mc = MongodbClient(set_name)
	def run(self):
		for callback_label in range(self.pg.__FunCount__):
			callback = self.pg.__FuncName__[callback_label]
			proxies = self.pg.get_proxies(callback)
			for proxy in proxies:
				self.mc.add(proxy)
class thread_Getter(Thread):
	def run(self):
		set_name = self._args
		Getter(set_name).run()
if __name__ == '__main__':
	# obj = Getter(set_name)
	# obj.run()
	set_names = ['shtproxy','jbsproxy']
	for set_name in set_names:
		t = thread_Getter(args=set_name)
		t.start()