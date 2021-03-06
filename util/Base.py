# coding:utf-8
import requests
import json
import random
import time
from hashlib import md5


class RunMain:

	def getMd5(self):
		#对登录密码num进行md5加密,返回密文
		num = 'midea_fridge_2020'
		MD5_password = md5(num.encode('utf8')).hexdigest()
		return MD5_password

	def get_token(self):
		MD5_password = self.getMd5()
		url = 'https://yyjh-prod.mideav.com/web/webaccount/login'
		data = {
			'account': 'midea_yyjh',
			'password': MD5_password
		}
		headers = {}
		res = self.send_post(url,data,headers)
		tokenValue = res['dataId']
		return tokenValue

	def send_post(self,url,data,headers):
		#res = requests.request("post",url=url,json=data,headers=None).json()
		res = requests.post(url, json=data,headers=headers).json()
		return res

	def send_get(self,url,data,headers):
		res = requests.get(url=url, data=data,headers=headers).json()
		return res

	def run_main(self,url,method,data,headers):
		res = None
		if method == 'get':
			res = self.send_get(url, data, headers)
		else:
			res = self.send_post(url, data, headers)
		return res	

if __name__ == '__main__':
	run = RunMain()
	#食材分类-添加
	url = 'https://yyjh-prod.mideav.com/web/foodType/insert'
	data = {'foodTypeName':'测试数据2'}
	headers = {'Content-Type': 'application/json;charset=UTF-8','token': run.get_token()}
	print run.run_main(url,'post',data,headers)





