from Proxypool.Mongodb_write import MongodbClient
from Spider.site_spider import Site_Getter
from Config.Configuration import Parameter
class Keep_data:
	def __init__(self):
		self.mc = MongodbClient()
		self.sg = Site_Getter()

	def writemongo(self,url):
		if url == Parameter.SHT_JP.value:
			nosql_name = "shtjp"
			self.sg.main(url,nosql_name)
		if url == Parameter.SHT_CHI.value:
			nosql_name = "shtchi"
			self.sg.main(url,nosql_name)
		if url == Parameter.SHT_UA.value:
			nosql_name = "shtua"
			self.sg.main(url,nosql_name)


if __name__ == '__main__':
	# url = Parameter.SHT_JP.value
	# urls = [Parameter.SHT_CHI.value,Parameter.SHT_JP.value,Parameter.SHT_UA.value]
	urls = [Parameter.SHT_UA.value]
	obj = Keep_data()
	for url in urls:
		print(url)
		obj.writemongo(url)