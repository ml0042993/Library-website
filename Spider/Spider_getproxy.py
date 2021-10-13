import requests

class Get_proxies:
	def __init__(self):
		self.url = "http://127.0.0.1:5000/random"

	def get_proxy(self):
		try:
			proxies = {}
			response = requests.get(self.url)
			if response.status_code == 200:
				# print(response.text)
				proxies['http'] = response.text
				return proxies
		except ConnectionError:
			return None

if __name__ == '__main__':
	obj = Get_proxies()
	print(obj.get_proxy())