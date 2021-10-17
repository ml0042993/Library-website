from enum import Enum#将常量变为枚举型
import datetime
class Parameter(Enum):#x枚举需要通过.value取值
	TIME_TAP = str(datetime.date.today())
	# TIME_TAP = str(datetime.date.today() - datetime.timedelta(days=1))#昨天的时间

	HEARD = {
	'Connection': 'close',#每次数据传输前客户端要和服务器建立TCP连接，为节省传输消耗，默认为keep-alive，即连接一次，传输多次，然而在多次访问后不能结束并回到连接池中，导致不能产生新的连接
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
	}
	# TEST_URL_BAD = "https://www.baidu.com/"

	TEST_URL_SHT = "https://rewrfsrewr.xyz/"
	TEST_URL_JBS = "https://www.javbus.com/"
	SET_NAME = ['shtproxy', 'jbsproxy']
	#进程的开关变量
	SPIDER_ENABLED = False
	TESTER_ENABLED = True
	GETTER_ENABLED = True
	API_ENABLED = False


	SHT_HOME = 'https://rewrfsrewr.xyz'
	SHT_JP='https://rewrfsrewr.xyz/forum-103-{}.html'
	SHT_CHI='https://rewrfsrewr.xyz/forum-2-{}.html'
	SHT_UA='https://rewrfsrewr.xyz/forum-38-{}.html'
	MONGOCLIENT = "mongodb://spider:jianxiong@192.168.1.123:27017/spider"
	# MONGOCLIENT = "mongodb://spider:jianxiong@192.168.71.129:27017/spider"