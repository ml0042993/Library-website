from Proxypool.Mongodb_write import MongodbClient
from Spider.site_spider import Site_Getter
from Config.Configuration import Parameter
class Keep_data:
	def __init__(self):
		self.mc = MongodbClient()
		self.sg = Site_Getter()

	def writemongo(self,url):

		for mess in self.sg.main(url):
			self.mc.keep_sht_CHI(mess)

if __name__ == '__main__':
	url = Parameter.SHT.value
	obj = Keep_data()
	obj.writemongo(url)