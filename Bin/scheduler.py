from multiprocessing import Process
from Proxypool.Proxypool_api import app
from Proxypool.Proxypool_saveproxy import thread_Getter as gtg
from Proxypool.Proxypool_tester import thread_Getter as ttg
from Config.Configuration import Parameter
from Spider.Spider_keepdata import Keep_data
import time

class Scheduler:
	def scheduler_getter(self,cycle = 1800):
		# getter = thread_Getter()
		while True:
			print("开始抓取代理")
			set_names = Parameter.SET_NAME.value
			for set_name in set_names:
				t = gtg(args=set_name)
				t.start()
			print("完成抓取代理")
			time.sleep(cycle)

	def scheduler_tester(self,cycle = 40):
		while True:
			print('测试器开始运行')
			set_names = Parameter.SET_NAME.value
			for set_name in set_names:
				t = ttg(args=set_name)
				t.start()
			time.sleep(cycle)

	def scheduler_keepdata(self):
		keeper = Keep_data()
		urls = [Parameter.SHT_CHI.value, Parameter.SHT_JP.value, Parameter.SHT_UA.value]
		for url in urls:
			print(url)
			keeper.writemongo(url)
		print("入库完成")
	def scheduler_api(self):
		app.run()

	def run(self):
		print("代理池开始运行")
		global getter_process,api_process,tester_process,keeper_process
		# try:
		if Parameter.GETTER_ENABLED.value:
			getter_process = Process(target=self.scheduler_getter)
			getter_process.start()
			# getter_process.join()
		if Parameter.API_ENABLED.value:
			api_process = Process(target=self.scheduler_api)
			api_process.start()
			# api_process.join()
		if Parameter.TESTER_ENABLED.value:
			tester_process = Process(target=self.scheduler_tester)
			tester_process.start()
			# tester_process.join()
		if Parameter.SPIDER_ENABLED.value:
			keeper_process = Process(target=self.scheduler_keepdata)
			keeper_process.start()
			keeper_process.close()
			# tester_process.join()
		getter_process.join()
		api_process.join()
		tester_process.join()
		keeper_process.join()
		# finally:
		# 	getter_process.join()
		# 	api_process.join()
		# 	tester_process.join()
if __name__ == '__main__':
	obj = Scheduler()
	obj.run()