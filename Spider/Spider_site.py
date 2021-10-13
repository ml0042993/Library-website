from Core.Core_pyquery import Get_pyqueryhtml
from Config.Configuration import Parameter
from Spider.Spider_getproxy import Get_proxies
from Core.Core_Mongodb import MongodbClient
import re

class Site_Getter:
	def __init__(self):
		self.gp = Get_pyqueryhtml()
		self.mc = MongodbClient()
		# self.proxy = Get_proxies().get_proxy()
		# self.TIME = time.strftime("%Y-%m-%d", time.localtime())
		self.Today = Parameter.TIME_TAP.value
		self.page = 1
		self.tap = '([^\x00-\xff]+[\x20]*[^\x00-\xff]*|\S*)'
	def get_html(self,url):
		try:
			new_proxy = Get_proxies().get_proxy()
			html = self.gp.Get_html(url,new_proxy)
			return html
		except Exception as e:
			# print(e.args)
			print("重新获取" + url)
			self.get_html(url)
	def construction_sht_base(self,html):
		'''
		获取子版块的内容，格式化入库内容
		:param html:
		:return:
		'''
		ths = html('.new').parent()
		trs = ths('tr').items()
		judge_tap = None
		taps = 0
		# print("最后一个日期是："+trs[-1](".by span span").attr("title"))
		for tr in trs:
			save_json ={}
			part_url = tr(".num a").attr('href')
			save_json['Real_url'] = "{}/{}".format(Parameter.SHT_HOME.value,part_url)
			save_json['date_info'] = tr(".by span span").attr("title")
			judge_tap = tr(".by span span").attr("title")
			taps += 1
			if save_json['date_info'] == self.Today:
				# print(save_mongo)
				yield save_json,True
			else:continue
		if judge_tap == self.Today:
			return self.Today,False

	def get_sht_detail(self,htmls):
		'''
		获取帖子实际内容,并进行入库前格式化
		:param htmls:
		:return:
		'''
		save_message = {}
		save_message['Title'] = htmls("#thread_subject").text()

		res = htmls(".t_f").text()
		if re.match(r"【影片名称】："+self.tap,res):
			save_message['Movie'] = re.match(r"【影片名称】："+self.tap,res).group(1)
		if re.search(r"【出演演员】："+self.tap,res):
			save_message['Actor'] = re.search(r"【出演女优】："+self.tap,res).group(1)
		if re.search(r"【影片格式】："+self.tap,res):
			save_message['Format'] = re.search(r"【影片格式】："+self.tap,res).group(1)
		if re.search(r"【影片大小】："+self.tap,res):
			save_message['Size'] = re.search(r"【影片大小】："+self.tap,res).group(1)

		imgs_url = htmls(".t_f img").items()
		imgs = []
		for img in imgs_url:
			img_url = img.attr("file")
			imgs.append(img_url)
		save_message["ImgsUrl"] = imgs

		save_message['magnet'] = htmls(".t_f .blockcode li").text()
		return save_message
	def read_mongo(self,Nosql_name,query_builder):
		for url in self.mc.read_Nosql(Nosql_name,query_builder):
			yield url


	def spider_judge_htmls(self,urls,nosql_name):
		'''
		获取帖子实际html源文档，并调用格式化函数get_sht_detailget_sht_detail()进行格式化，
		最后调用入库函数keep_sht_core()
		:param urls: ({'Real_url': 'url地址', 'date_info': '日期'}, True)
		:param nosql_name: 数据库名称
		:return:
		'''
		# for urls in self.read_mongo(nosql_name):
		try:
			url = urls.get("Real_url")
			find_info = urls
			# find_info["Real_url"] = url
			htmls = self.get_html(url)
			save_message = self.get_sht_detail(htmls)
			# print(save_message)
			self.mc.keep_sht_core(nosql_name,find_info,save_message)
			print("完成获取"+url)
		except TypeError:
			self.spider_judge_htmls(urls,nosql_name)

	def dispose_html(self,html,taps,home_url):
		'''
		从mongo中取出要爬取的网页地址
		:param html: 得到的实际网页document内容
		:param taps: 使用上级页面提供查询匹配的条件
		:param home_url:'https://rewrfsrewr.xyz/forum-103-{}.html'
		:return:
		'''
		for save_json in self.construction_sht_base(html):
			print(save_json)
			if save_json[1] == True:#save_json是一个元组
				self.mc.mongo_keep_sht(save_json[0], taps=taps)
			if save_json[1] == False:
				# 如果当前页面的最后一个日期是本日，则开始下一页获取
				print("最后一个链接的日期为：{}".format(save_json[0]))
				self.page += 1
				self.spider_get_homeurl(home_url)

	def spider_get_homeurl(self,home_url,page=None):
		"""
		传入子版块url，获取子版块内的各个帖子的当日url地址
		:param home_url: 未format的子版块url'https://rewrfsrewr.xyz/forum-103-{}.html'
		:param page:设置动态页码，提供翻页条件
		:param taps:taps=home_url是向mongo提供入库的条件同disport_html传入
		:return: None
		"""
		page = self.page
		try:
			html = self.get_html(home_url.format(page))
			self.dispose_html(html,taps=home_url,home_url=home_url)
		except Exception as e:
			print(e.args)
	def spider_allsave_mongo(self,nosql_name):
		'''
		遍历mongo中存储的子版块帖子的url列表，逐个传入spider_judge_htmls()获取关键内容，进行构造，再入库
		:param nosql_name: 数据库名称
		:return:
		'''
		query_builder = {"date_info":self.Today}
		for urls in self.read_mongo(nosql_name,query_builder=query_builder):
			self.spider_judge_htmls(urls,nosql_name,)
	def main(self,home_url,nosql_name):
		'''
		:param home_url:未format的子版块url
		:param nosql_name:数据库名称
		:return:
		'''
		self.spider_get_homeurl(home_url)
		self.spider_allsave_mongo(nosql_name)

if __name__ == '__main__':
	obj = Site_Getter()
	obj.main('https://rewrfsrewr.xyz/forum-103-1.html','shtjp')