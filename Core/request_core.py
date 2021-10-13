import requests
from urllib3.util.retry import Retry
from requests.adapters import HTTPAdapter
from pyquery import PyQuery as pq
from Config.Configuration import Parameter
# 得到输入网页的源代码
class Requert_init:
	def Get_requers(self,url,proxies=None):
		try:
			# process_html=requests.get(url,headers=Parameter.HEARD.value,proxies=proxies,timeout=20)
			session = requests.Session()
			retry = Retry(connect=3, backoff_factor=0.5)
			adapter = HTTPAdapter(max_retries=retry)
			session.mount('http://', adapter)
			session.mount('https://', adapter)
		# encoding是从http中的header中的charset字段中提取的编码方式，若header中没有charset字段则默认为ISO-8859-1编码模式，则无法解析中文
			# ，这是乱码的原因。
		# apparent_encoding会从网页的内容中分析网页编码的方式，所以apparent_encoding比encoding更加准确。当网页出现乱码时可以把
			# apparent_encoding的编码格式赋值给encoding。
			process_html = session.get(url,headers=Parameter.HEARD.value,proxies=proxies,verify=False,timeout=20)
			process_html.encoding = process_html.apparent_encoding#解决乱码问题
			return process_html#返回首页的html源代码
		except(ConnectionError):
			print("连接超时，重新获取")
			# self.Get_requers(url)
		except Exception as e:
			print("未知错误,重新获取")
			print(e.args)
			# self.Get_requers(url)
	def Get_pyquery(self,process_html):
		'''
		将源文件初始化为PyQuery对象
		:return: None
		'''
		pyquery_doc = pq(process_html.text)
		return pyquery_doc
