from enum import Enum#将常量变为枚举型
class Parameter(Enum):#x枚举需要通过.value取值
	HEARD = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36',
	}
	# TEST_URL = "https://www.baidu.com/"
	TEST_URL = "https://rewrfsrewr.xyz/"
	TESTER_ENABLED = True
	GETTER_ENABLED = True
	API_ENABLED = True
	SHT_HOME = 'https://rewrfsrewr.xyz'
	SHT_JP='https://rewrfsrewr.xyz/forum-103-1.html'
	SHT_CHI='https://rewrfsrewr.xyz/forum-2-1.html'
	SHT_UA=''
	# MONGOCLIENT = "mongodb://spider:jianxiong@192.168.1.123:27017/spider"
	MONGOCLIENT = "mongodb://spider:jianxiong@192.168.71.129:27017/spider"