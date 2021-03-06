# coding:utf-8
import json


class CommonUtil:
	def is_contain(self, str_one, str_two):
		'''
		判断一个字符串是否再另外一个字符串中
		str_one:查找的字符串
		str_two：被查找的字符串
		'''
		flag = None
		#判断字符串str_one是否是unicode类型
		if isinstance(str_one, unicode):
			#将unicodea类型转化为字符串类型
			str_one = str_one.encode('unicode-escape').decode('string_escape')
			return cmp(str_one, str_two)
		if str_one in str_two:
			flag = True
		else:
			flag = False
		return flag

	def is_equal_dict(self, dict_one, dict_two):
		'''
		判断两个字典是否相等
		'''
		if isinstance(dict_one, str):
			dict_one = json.loads(dict_one)
		if isinstance(dict_two, str):
			dict_two = json.loads(dict_two)
		return cmp(dict_one, dict_two)


if __name__ == '__main__':
	comU = CommonUtil()
	str_one='"uid":"123456","nickname":"zhaokang","123":123456"'
	str_two='"uid":"123456","nickname":"zhaokang"'
	print type(str_one)
	print comU.is_contain(str_one, str_two)
	print comU.is_contain(str_two, str_one)
	#print comU.is_equal_dict(str_one, str_two)