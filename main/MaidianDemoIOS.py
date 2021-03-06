# coding:utf-8
import json
import re
import copy

'''传参埋点关键字，从plugin_action.txt查询出，并返回str格式的埋点'''


class DemoM:
	def read(self):
		f = open('../dataconfig/plugin_action.txt')
		plugin_data = f.read()           # 返回数据类型为str
		# print plugin_data
		# 将字符串按照{}拆分后放入list中
		global list_data
		list_data = plugin_data.split('},')
		# list_data = re.split(r"(})",plugin_data)   #保留了分隔符},但是该分隔符被单独放在一起
		# print list_data[10]
		# print '----------------------------------'
		# print '文件包含埋点总数：',len(list_data)      #缓存文件中埋点数

	def str_to_dict(self):
		global dict_data
		dict_data = []
		i = -1
		while i < len(list_data)-2:
			i = i+1
			# print '第'+str(i+1)+'个埋点'
			data = list_data[i]+'}'
			# print data
			data = eval(data)
			# print data
			dict_data.append(data)
		return dict_data

	def find_str(self, a, b, c):
		# 只要找到1个符合条件的埋点就停止，继续找其它的埋点
		for i in range(0, len(list_data)-1):         # 只执行到10
			# print i
			if not (dict_data[i]['page_name'] == a and dict_data[i]['sub_action'] == b and dict_data[i]['prev_page_name'] == c):
				# print '-----------------this is true!-----------------------'
				continue
			else:
				# return dict_data[i]
				# return json.dumps(dict_data[i],ensure_ascii=False,sort_keys=True,indent=2)
				res = json.dumps(dict_data[i], ensure_ascii=False, sort_keys=True)
				return res.replace(" ", "")

	# 此方法废弃
	def find_str1(self, a, b, c):
		# print len(list_data)
		# print type(dict_data[10])
		for i in range(0, len(list_data)-1):         # 只执行到10
			# print i
			if dict_data[i]['page_name'] == a and dict_data[i]['sub_action'] == b and dict_data[i]['prev_page_name'] == c:
				# print '-----------------this is true!-----------------------'
				print dict_data[i]
				print type(dict_data[i])
			else:
				print '不符合'


if __name__ == '__main__':
	
	demo=DemoM()
	print demo.read()
	demo.str_to_dict()
	res1 = demo.find_str('HfridgeMainPage', 'refrigeratorChange', 'mideaHomePage')    # 有两个符合
	res2 = demo.find_str('smartCentrePage', 'page_view', 'fridgeMainpage')
	res3 = demo.find_str('HfridgeMainPage', 'frozenOn', 'mideaHomePage')
	res = demo.find_str('', '', '')
	# print res3
	print res3
	# print res
	# print type(res1)
	# print type(demo.find_str('smartCentrePage','page_view','fridgeMainpage'))
	# demo.find_str('morePage','page_view','fridgeMainpage')



