from Core.Core_Mongodb import MongodbClient
from Config.Configuration import Parameter
from threading import Thread
import aiohttp
import asyncio
import math
class Tester:
	def __init__(self,set_name):
		self.mongo = MongodbClient(set_name)
		self.set_name = set_name

	async def test_single_proxy(self,proxy_ip,port):
		conn = aiohttp.TCPConnector(ssl=False)
		async with aiohttp.ClientSession(connector=conn) as session:
			try:
				if isinstance(proxy_ip,bytes):
					proxy_ip = proxy_ip.decode('utf-8')
				real_proxy = 'http://{}:{}'.format(proxy_ip,port)
				if self.set_name == 'shtproxy':
					url = Parameter.TEST_URL_SHT.value
				if self.set_name == 'jbsproxy':
					url = Parameter.TEST_URL_JBS.value
				async with session.get(url, proxy=real_proxy, timeout=10) as response:
					# print(response.status)
					if response.status == 200:
						self.mongo.max(proxy_ip)
						print("代理可用",proxy_ip)
					else:
						self.mongo.decrease(proxy_ip)
						# print("代理不可用",proxy_ip)
			except Exception as e:
				# print(e.args)
				self.mongo.decrease(proxy_ip)
				# print("请求失败，代理不可用",proxy_ip)
	async def main(self):
		try:
			# tasks=[]
			taps = math.ceil(self.mongo.count()/50)+1
			for tap in range(1,taps):
				tasks = []
				proxies = self.mongo.all().skip(50*tap-50).limit(50)
				for result in proxies:
					proxy_ip=result['Ip']
					port=result['Port']
					task = asyncio.create_task(self.test_single_proxy(proxy_ip,port))
					tasks.append(task)
				await asyncio.wait(tasks,timeout=11)
		except Exception as e:
			print("woring",e.args)

	def run(self):
		asyncio.run(self.main())
class thread_Getter(Thread):
	def run(self):
		set_name = self._args
		Tester(set_name).run()
if __name__ == '__main__':
	# obj = Tester()
	# obj.run()
	set_names = ['shtproxy', 'jbsproxy']
	for set_name in set_names:
		t = thread_Getter(args=set_name)
		t.start()