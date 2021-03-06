# coding:utf-8


class global_var:
	# case_id
	version = '0'
	page_name = '6'
	sub_action = '7'
	prev_page_name = '8'
	get_result = '9'

def get_page_name():
	return global_var.page_name

def get_sub_action():
	return global_var.sub_action

def get_prev_page_name():
	return global_var.prev_page_name

def get_result():
	return global_var.get_result


