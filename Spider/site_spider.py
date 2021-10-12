from Core.pyquery_date import Get_pyqueryhtml
from Config.Configuration import Parameter
from Spider.get_proxy import Get_proxies
from Proxypool.Mongodb_write import MongodbClient
import re
import datetime
class Site_Getter:
	def __init__(self):
		self.gp = Get_pyqueryhtml()
		self.mc = MongodbClient()
		# self.proxy = Get_proxies().get_proxy()
		# self.TIME = time.strftime("%Y-%m-%d", time.localtime())
		self.Today = datetime.date.today()
		self.Yseterday = self.Today - datetime.timedelta(days=1)
		self.tap = '([^\x00-\xff]+[\x20]*[^\x00-\xff]*|\S*)'
	def get_html(self,url):
		new_proxy = Get_proxies().get_proxy()
		try:
			html = self.gp.Get_html(url,new_proxy)
			return html
		except Exception as e:
			print(e.args)
			print("get_html function is url:" + url)
			self.get_html(url)
	def get_sht_base(self,html):
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
			if save_json['date_info'] == str(self.Today):
				# print(save_mongo)
				yield save_json,True
			else:continue
		if judge_tap == self.Today:
			return self.Today,False

	def get_sht_detail(self,htmls):
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
	def read_mongo(self,Nosql_name):
		for url in self.mc.read_Nosql(Nosql_name):
			yield url


	def main(self,target_url,nosql_name):
		'''
		:param target_url:上级
		:param nosql_name:
		:return:
		'''
		html = self.get_html(target_url)
		try:
			for save_json in self.get_sht_base(html):
				print(save_json)
				if save_json[1] == True:
					self.mc.keep_sht(save_json[0],taps=target_url)
				if save_json[1] == False:
					#如果当前页面的最后一个日期是本日，则开始下一页获取
					print("最后一个链接的日期为：{}".format(save_json[0]))

		except Exception as e:
			print(e.args)

		for urls in self.read_mongo(nosql_name):
			url = urls.get("Real_url")
			find_info = urls
			# find_info["Real_url"] = url
			htmls = self.get_html(url)
			save_message = self.get_sht_detail(htmls)
			# print(save_message)
			self.mc.keep_sht_core(nosql_name,find_info,save_message)




if __name__ == '__main__':
	obj = Site_Getter()
	obj.main('https://rewrfsrewr.xyz/forum-103-1.html','shtjp')