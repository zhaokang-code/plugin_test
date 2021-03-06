# coding:utf-8
from MaidianDemoIOS import DemoM
from data.get_data import GetData

'''1.从测试报告excel中读取埋点关键字，然后从缓存文件中查询出对应的埋点
   2.运行前检查operation_excel中的上传文件
'''


class Method:
	def __init__(self):
		self.demo = DemoM()
		self.get = GetData()

	# 从测试报告excel中，读取行数及每行的埋点关键字，使用读取的埋点关键字从txt文件中检索出符合条件的埋点数据
	def run_main(self):
		rows_count = self.get.get_case_lines()
		for i in range(1, rows_count):
			print 'case的埋点数据：',i
			page_name = self.get.get_page_name(i)
			sub_action = self.get.get_sub_action(i)
			prev_page_name = self.get.get_prev_page_name(i)
			self.demo.read()
			self.demo.str_to_dict()
			data = self.demo.find_str(page_name, sub_action, prev_page_name)
			print data


if __name__ == '__main__':
	run = Method()
	run.run_main()


