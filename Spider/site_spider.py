from Core.pyquery_date import Get_pyqueryhtml
from Config.Configuration import Parameter
from Spider.get_proxy import Get_proxies
import re
import datetime
class Site_Getter:
	def __init__(self):
		self.gp = Get_pyqueryhtml()
		# self.proxy = Get_proxies().get_proxy()
		# self.TIME = time.strftime("%Y-%m-%d", time.localtime())
		self.Today = datetime.date.today()
		self.Yseterday = self.Today - datetime.timedelta(days=1)
		self.tap = '([^\x00-\xff]+[\x20]*[^\x00-\xff]*|\S*)'

	def get_sht_base(self,url,proxy):
		# proxy = Get_proxies().get_proxy()
		url = url
		html = self.gp.Get_html(url,proxy)
		if html:
			ths = html('.new').parent()
			trs = ths('tr').items()

			for tr in trs:
				save_mongo ={}
				part_url = tr(".num a").attr('href')
				save_mongo['Real_url'] = "{}/{}".format(Parameter.SHT_HOME.value,part_url)
				save_mongo['date_info'] = tr(".by span span").attr("title")
				if save_mongo['date_info'] == str(self.Today):
					# print(save_mongo)
					yield save_mongo
				else:continue
	def get_sht_detail(self,message,proxy):

		save_message = message
		url = save_message['Real_url']
		# save_message={}
		# url = 'https://rewrfsrewr.xyz/thread-635325-1-1.html'
		try:
			if url:
				htmls = self.gp.Get_html(url, proxy)

				if htmls:
					save_message['Title'] = htmls("#thread_subject").text()

					res = htmls(".t_f").text()
					if re.match(r"【影片名称】："+self.tap,res):
						save_message['Movie'] = re.match(r"【影片名称】："+self.tap,res).group(1)
					if re.search(r"【出演女优】："+self.tap,res):
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
			else:print("未获取有效链接")
		except AttributeError:
			print("未获取页面，重新获取")
			new_proxy = Get_proxies().get_proxy()
			self.get_sht_detail(message,new_proxy)

	def main(self,url,):
		proxy = Get_proxies().get_proxy()
		try:
			for site in self.get_sht_base(url,proxy):
				print("真正获取{}".format(site['Real_url']))
				message = self.get_sht_detail(site,proxy)
				yield message
		except AttributeError:
			print("未获取页面，重新获取")
			self.main(url)


if __name__ == '__main__':
	obj = Site_Getter()
	obj.main('https://rewrfsrewr.xyz/forum-103-1.html')