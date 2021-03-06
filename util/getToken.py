# coding:utf-8
import random
import time
from hashlib import md5
from Crypto.Cipher import AES
from binascii import b2a_hex, a2b_hex
from operation_excel import OperationExcel
from data.get_data import GetData


class GetToken:

	def __init__(self):
		self.opera_excel = OperationExcel()
		self.data = GetData()

	# 生成6位随机数
	def nonce(self):
		return random.randint(100000, 999999)

	# 生成时间戳
	def time_stamp(self):
		time_stamp = int(round(time.time()*1000))
		return time_stamp

	# 以拼接后的字符串明文为参数
	def get_token(self, num):
		# 对字符串进行md5加密
		MD5 = md5(num.encode('utf8')).hexdigest()
		# AES加密
		key = '20160613646aBcDW'
		cryptos = AES.new(key, AES.MODE_ECB)
		padding = lambda s: s + (16 - len(s) % 16) * chr(16 - len(s) % 16)
		ciphertext = cryptos.encrypt(padding(MD5).encode("utf-8"))
		token = b2a_hex(ciphertext)
		return token

	# 传入行号就可以得到token
	def get_token2(self, row):
		# 获得excel中的拼接字符串
		num = self.data.get_joint_value(row)
		print num
		if num != None:
			token_value = self.get_token(num)
		else:
			token_value = ''
		return token_value


if __name__ == '__main__':
	tools = GetToken()
	# num = 'nonce123456time_stamp123321'
	# 传入行号就可以得到token
	print tools.get_token2(1)

