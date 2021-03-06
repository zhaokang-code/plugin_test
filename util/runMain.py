# coding:utf-8
import requests
import json
import random
import time
from util.getToken import GetToken

class RunMain:
	
	# def __init__(self):
		#res = self.run_main(url, method, data)
		#self.get = Get_Token()

	def send_get(self, url, data):
		res = requests.get(url=url, data=data).json()
		return res
		
	def send_post(self, url, data):
		res = requests.post(url=url, data=data).json()    #.text
		#print type(res)
		return res          

	def run_main(self, url, method,data=None):
		res = None
		if method == 'GET':
			res = self.send_get(url, data)
		else:
			res = self.send_post(url, data)
		return res

	def get(self,num):
		get = GetToken()
		return get.get_token(num)

if __name__ == '__main__':

	run = RunMain()
	num = 'foodName'+u'苹果'+'nonce123456time_stamp123321'
	token = run.get(num)
	print token
	url2 = 'https://fridge-api.mideav.com/fridge/FoodDetail/searchList'  # 食材查询/foodName
	data2 = {"foodName": "苹果", "time_stamp": 123321, "token": token, "nonce": 123456}
	res = run.run_main(url2, 'post', data2)
	print res
	print json.dumps(res, ensure_ascii=False, sort_keys=True, indent=2)