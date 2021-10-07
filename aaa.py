# # # import asyncio
# # # import requests
# # # import concurrent.futures as futures
# # # async def download_image(url):# 发送网络请求，下载图片（遇到网络下载图片的IO请求，自动化切换到其他任务）
# # # 	print("开始下载:", url)
# # # 	loop = asyncio.get_event_loop()
# # # 	# requests模块默认不支持异步操作，所以就使用线程池来配合实现了。
# # # 	# future = loop.run_in_executor(None, requests.get, url)
# # #     # response = await future
# # # 	with futures.ThreadPoolExecutor() as pool:
# # # 		future = loop.run_in_executor(pool,requests.get,url)
# # # 		response = await future
# # # 		print('下载完成')
# # # 	# 图片保存到本地文件
# # # 	file_name = url.rsplit('_')[-1]
# # # 	with open(file_name, mode='wb') as file_object:
# # # 		file_object.write(response.content)
# # # if __name__ == '__main__':
# # # 	url_list = [
# # #         'https://www3.autoimg.cn/newsdfs/g26/M02/35/A9/120x90_0_autohomecar__ChsEe12AXQ6AOOH_AAFocMs8nzU621.jpg',
# # #         'https://www2.autoimg.cn/newsdfs/g30/M01/3C/E2/120x90_0_autohomecar__ChcCSV2BBICAUntfAADjJFd6800429.jpg',
# # #         'https://www3.autoimg.cn/newsdfs/g26/M0B/3C/65/120x90_0_autohomecar__ChcCP12BFCmAIO83AAGq7vK0sGY193.jpg'
# # #     ]
# # # 	tasks = [download_image(url) for url in url_list]
# # # 	loop = asyncio.get_event_loop()
# # # 	loop.run_until_complete( asyncio.wait(tasks) )
# # import pymongo
# #
# # db = pymongo.MongoClient("mongodb://spider:jianxiong@192.168.1.123:27017/spider")['spider']
# # # result = db.proxypool.find({},{'Ip':1,'Port':1,"_id":0})
# # # for i in result:
# # # 	print(':'.join([i["Ip"],i["Port"]]))
# # aaa = db.proxypool.find({"Ip":"212.22.69.119"},{'Score':1,"_id":0})[0]["Score"]
# # print(aaa)
# import time
# from multiprocessing import Process
#
# def f(name):
# 	while True:
# 		print('hello', name)
# 		time.sleep(10)
#
# if __name__ == '__main__':
#
# 	p = Process(target=f, args=('bob',))
# 	p.start()
# 	p1 = Process(target=f, args=('111',))
# 	p1.start()
# 	# p_lst.append(p)
#     # [p.join() for p in p_lst]
# 	print('父进程在执行')
# 引入 datetime 模块
import datetime


def getYesterday():
	today = datetime.date.today()
	oneday = datetime.timedelta(days=1)
	yesterday = today - oneday
	return yesterday


# 输出
print(str(getYesterday()))