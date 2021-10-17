# class aa:
# 	def __init__(self):
# 		self.ss = 1
# 	def add(self):
# 		self.ss+=1
#
# obj = aa()
# obj.add()
# print(obj.ss)
# import multiprocessing
# cout=multiprocessing.cpu_count()
# print(cout)
from threading import Thread
import time
class AA:
	def __init__(self,tap):
		self.tap = tap

	def fun(self):
		print("这是",self.tap)
		time.sleep(5)
		print(self.tap,"结束")

class BB(Thread):
	def run(self):
		tap = self._args
		AA(tap).fun()
if __name__ == '__main__':
	taps = ['第一个','第二个']

	for tap in taps:
		t = BB(args=tap)
		t.start()
		t.join()