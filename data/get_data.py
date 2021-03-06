# coding:utf-8
from util.operation_excel import OperationExcel
from util.operation_json import OperetionJson
# from util.connect_db import OperationMysql
import data_config


class GetData:
	def __init__(self):
		self.opera_excel = OperationExcel()

	# 去获取excel行数,就是我们的case个数
	def get_case_lines(self):
		return self.opera_excel.get_lines()

	# 获取page_name
	def get_page_name(self, row):
		col = int(data_config.get_page_name())
		page_name = self.opera_excel.get_cell_value(row, col)
		return page_name

	# 获取sub_action
	def get_sub_action(self,row):
		col = int(data_config.get_sub_action())
		sub_action = self.opera_excel.get_cell_value(row, col)
		return sub_action

	# 获取prev_page_name
	def get_prev_page_name(self,row):
		col = int(data_config.get_prev_page_name())
		prev_page_name = self.opera_excel.get_cell_value(row, col)
		return prev_page_name

	# -----------------------------------------------------------------------------
	# 获取url
	def get_request_url(self,row):
		col = int(data_config.get_url())
		url = self.opera_excel.get_cell_value(row, col)
		return url

	# 获取是否执行
	def get_is_run(self, row):
		flag = None
		col = int(data_config.get_run())         # col已经在data_config中被写死了
		run_model = self.opera_excel.get_cell_value(row, col)
		if run_model == 'Yes':
			flag = True
		else:
			flag = False
		return flag

	# 获取请求方式
	def get_request_method(self, row):
		col = int(data_config.get_run_way())
		request_method = self.opera_excel.get_cell_value(row,col)
		return request_method

	# 是否携带header
	def is_header(self, row):
		col = int(data_config.get_header())
		header = self.opera_excel.get_cell_value(row, col)
		if header != 'Yes':
			return header
		else:
			return None

	# 获取到excel表中请求数据关键字
	def get_request_data(self, row):
		col = int(data_config.get_data())
		data = self.opera_excel.get_cell_value(row, col)
		if data == '':
			return None
		return data

	# 通过excel中关键字拿到配置文件中的请求数据
	def get_data_for_json(self, row):
		opera_json = OperetionJson()
		request_data = opera_json.get_data(self.get_request_data(row))
		return request_data

	# 获取预期结果
	def get_expcet_data(self, row):
		col = int(data_config.get_expect())
		expect = self.opera_excel.get_cell_value(row, col)
		if expect == '':
			return None
		return expect

	# 通过sql获取预期结果
	'''
	def get_expcet_data_for_mysql(self, row):
		op_mysql = OperationMysql()
		sql = self.get_expcet_data(row)
		res = op_mysql.search_one(sql)
		return res.decode('unicode-escape')
	'''
	# 结果回写
	def write_result(self, row, value):
		col = int(data_config.get_result())
		self.opera_excel.write_value(row, col, value)

	# 不通过的case执行结果回写
	def write_res(self, row, value):
		col = int(data_config.get_res_value())
		self.opera_excel.write_value(row, col, value)

	# 判断是否有case依赖
	def is_depend(self, row):
		col = int(data_config.get_case_depend())
		depend_case_id = self.opera_excel.get_cell_value(row, col)
		if depend_case_id == "":
			return None
		else:
			return depend_case_id

	# 获取依赖数据的key
	def get_depend_key(self,row):
		col = int(data_config.get_data_depend())       # 中间的depend  第7列
		depent_key = self.opera_excel.get_cell_value(row, col)
		if depent_key == "":
			return None
		else:
			return depent_key

	# 获取数据依赖字段
	def get_depend_field(self, row):
		col = int(data_config.get_field_depend())
		data = self.opera_excel.get_cell_value(row, col)
		if data == "":
			return None
		else:
			return data

	# 获取拼接字符串（获取token的原始值num）
	def get_joint_value(self,row):
		col = int(data_config.get_joint_value())
		data = self.opera_excel.get_cell_value(row, col)
		if data == "":
			return None
		else:
			return data
	

if __name__ == '__main__':
	get = GetData()
	print get.get_case_lines()
	print get.get_page_name(1)         #case001的
	print get.get_sub_action(1)
	print get.get_prev_page_name(1)




