from Core.Core_Mongodb import MongodbClient
from Config.Configuration import Parameter as para
import aiohttp
import asyncio
import math
class Tester:
	def __init__(self):
		self.mongo = MongodbClient()


	async def test_single_proxy(self,proxy_ip,port):
		conn = aiohttp.TCPConnector(ssl=False)
		async with aiohttp.ClientSession(connector=conn) as session:
			try:
				if isinstance(proxy_ip,bytes):
					proxy_ip = proxy_ip.decode('utf-8')
				real_proxy = 'http://{}:{}'.format(proxy_ip,port)
				async with session.get(para.TEST_URL_SHT.value, proxy=real_proxy, timeout=10) as response:
					print(response.status)
					if response.status == 200:
						self.mongo.max(proxy_ip)
						print("代理可用",proxy_ip)
					else:
						self.mongo.decrease(proxy_ip)
						print("代理不可用",proxy_ip)
			except Exception as e:
				# print(e.args)
				self.mongo.decrease(proxy_ip)
				print("请求失败，代理不可用",proxy_ip)
	async def main(self):
		try:
			# tasks=[]
			taps = math.ceil(self.mongo.count()/20)+1
			for tap in range(1,taps):
				tasks = []
				proxies = self.mongo.all().skip(20*tap-20).limit(20)
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

if __name__ == '__main__':
	obj = Tester()
	obj.run()