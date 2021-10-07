from Core.request_core import Requert_init

class Get_pyqueryhtml:
	def __init__(self):
		self.pyquery_mess = Requert_init()

	def Get_html(self,url,proxies=None):
		requert_mess = self.pyquery_mess.Get_requers(url,proxies)
		return self.pyquery_mess.Get_pyquery(requert_mess)