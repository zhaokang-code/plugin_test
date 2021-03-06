# coding:utf-8
import json
import re
import copy

'''
1)从logcat文件夹中读取埋点信息
2)根据传入的关键字查询出str格式的埋点
'''



class DemoM:
	def read(self):
		f = open('../dataconfig/log1026.txt')
		plugin_data = f.read()                      # 返回数据类型为str
		list = re.findall(r'[{](.*?)[}]', plugin_data)   # 将字符串中括号中的内容取出
		# print list[30]
		# print len(list)
		global list_data
		list_data = []
		for i in list:
			if len(i)>250 and len(i)<770:
				i = '{'+i+'}'
				list_data.append(i)
		# print len(list_data)
		# print type(list_data[0])
		return list_data

	def str_to_dict_android(self):
		# 使用eval函数将str转化为dict,形如字典的str数据中不能出现"value"值为空的情况data = eval(data)
		# 筛选长度200到300的数据时使用   type(list_data[0])
		global dict_data
		dict_data = []
		i = -1
		while i < len(list_data)-1:
			i = i+1
			data = list_data[i]
			# data = json.loads(data)
			data = eval(data)	
			dict_data.append(data)
		return dict_data

	def find_str(self, a, b, c):
		# print dict_data[20]
		# 只要找到1个符合条件的埋点就停止，继续找其它的埋点
		for i in range(0,len(list_data)-1):         # 只执行到10
			# print i
			if not (dict_data[i]['pageName']==a and dict_data[i]['subAction']==b and dict_data[i]['prev_page_name'] ==c):
				# print '-----------------this is true!-----------------------'
				continue
			else:
				# return dict_data[i]
				# return json.dumps(dict_data[i],ensure_ascii=False,sort_keys=True,indent=2)
				res = json.dumps(dict_data[i],ensure_ascii=False,sort_keys=True)                                      
				return res.replace(" ", "")

	def str_to_dict_android1(self):
		# 使用eval函数将str转化为dict,形如字典的str数据中不能出现"value"值为空的情况data = eval(data)
		# 筛选长度600到800的数据时使用
		global dict_data
		dict_data = []
		i = -1
		while i< len(list_data)-1:
			i = i+1
			data = list_data[i]
			data = json.loads(data)		
			dict_data.append(data)
		return dict_data


if __name__ == '__main__':
	
	demo=DemoM()
	print demo.read()
	print '---------------------------分隔符-----------------------------'
	# demo.str_to_dict_android()
	# res = demo.find_str('HfridgeMainPage','frozenOff','mideaHomePage')
	# print res
	'''
	res1 = demo.find_str('IndexActivity','page_view','')
	res2 = demo.find_str('IndexActivity','page_view','')
	res = demo.find_str('HfridgeMainPage','frozenOff','mideaHomePage')
	print res1
	print res2
	'''




