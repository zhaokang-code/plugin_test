# -*- coding: utf-8 -*-
import MySQLdb.cursors
import json
from util.operation_excel import OperationExcel


class Report:

	def __init__(self):
		self.opers = OperationExcel()
		self.cur = self.conn_base()
		self.obj = self.get_data()
		self.data = self.base_data()

	def conn_base(self):
		# 连接数据库
		conn = MySQLdb.connect(
					host='localhost',
					port=3306,
					user='root',
					passwd='123456',
					# db='192.168.2.131',
					db='kangdata',
					charset='utf8',
					cursorclass=MySQLdb.cursors.DictCursor
					)
		cur = conn.cursor()
		return cur

	def get_data(self):	
		global num	
		num =self.cur.execute("select * from plugintest") # 查询数据库中全部埋点信息  得到一个元组
		# print num
		obj = self.cur.fetchall() #得到所有行的数据/元组
		return obj

	def base_data(self):
		global ids,page_names,touch_shows,page_locations,page_names,sub_actions,prev_page_names,ress
		ids=[]
		page_names=[]
		touch_shows=[]
		page_locations=[]
		page_names=[]
		sub_actions=[]
		prev_page_names=[]
		ress=[]
		for i in range(0,num):
			ids.append(self.obj[i]['id'])
			touch_shows.append(self.obj[i]['touch_show'])
			page_locations.append(self.obj[i]['page_location'])
			page_names.append(self.obj[i]['page_name'])
			sub_actions.append(self.obj[i]['sub_action'])
			prev_page_names.append(self.obj[i]['prev_page_name'])
			ress.append(self.obj[i]['res'])
		return ids,touch_shows,page_locations,page_names,sub_actions,prev_page_names,ress

	def write_to_excel(self):
		for i in range(1,num+1):
			print id
			self.opers.write_value(i, 0, ids[i-1])
			self.opers.write_value(i, 1, 'T0XCA')
			self.opers.write_value(i, 2, u'通用')
			self.opers.write_value(i, 3, touch_shows[i-1])
			self.opers.write_value(i, 4, page_locations[i-1])
			self.opers.write_value(i, 5, u'Ref_型号')
			self.opers.write_value(i, 6, '3.0.0')
			self.opers.write_value(i, 7, 'common')
			self.opers.write_value(i, 8, page_names[i-1])
			self.opers.write_value(i, 9, sub_actions[i-1])
			self.opers.write_value(i, 10, prev_page_names[i-1])
			self.opers.write_value(i, 11, ress[i-1])

	def conn_close(self):
		# 关闭数据库连接
		return self.conn.close()


if __name__ == '__main__':
	get = Report()
	get.write_to_excel()






 


