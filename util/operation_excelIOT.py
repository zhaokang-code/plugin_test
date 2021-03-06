# coding:utf-8
import xlrd
from xlutils.copy import copy
import json


class OperationExcel:
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataconfig/demoM.xls'
            self.sheet_id = 0
        self.data = self.get_data()

    # 获取sheets的内容
    def get_data(self):
        data = xlrd.open_workbook(self.file_name)
        tables = data.sheets()[self.sheet_id]
        return tables

    # 获取单元格的行数
    def get_lines(self):
        tables = self.data
        return tables.nrows
    # xlrd.open_workbook().sheets()[].nrows
    # xlrd.open_workbook().cell_value(row, col)
    # 获取某一个单元格的内容

    def get_cell_value(self, row, col):
        return self.data.cell_value(row, col)

    # 写入数据
    def write_value(self, row, col, value):

        # 写入excel数据row,col,value
        read_data = xlrd.open_workbook(self.file_name)
        write_data = copy(read_data)
        sheet_data = write_data.get_sheet(0)
        sheet_data.write(row, col, value)
        write_data.save(self.file_name)

    # 获取某一列的内容(输入列号后获取该列的全部内容,此处将列默认为第1列,返回第一列的全部列值)
    def get_cols_data(self, col_id=None):
            if col_id != None:
                cols = self.data.col_values(col_id)
            else:
                cols = self.data.col_values(0)
            return cols

    # 根据对应的caseid找到对应的行号
    def get_row_num(self, case_id):
        num = 0
        clols_data = self.get_cols_data()   # 不传参则默认为第1列，返回第一列全部列值list，算出case_001在list中的位置传给num
        for col_data in clols_data:
            if case_id in col_data:
                return num
            num = num+1

    # 根据行号，找到该行的内容                   (根据行号num获取依赖用例所在行的全部数据)
    def get_row_values(self, row):
        tables = self.data
        row_data = tables.row_values(row)
        return row_data

    # 根据对应的caseid 找到对应行的内容          
    def get_rows_data(self, case_id):
        row_num = self.get_row_num(case_id)
        rows_data = self.get_row_values(row_num)
        return rows_data


if __name__ == '__main__':
    opers = OperationExcel()
    # print opers.get_cell_value(1, 2)
    print opers.get_lines()   # 获取行数
    print opers.get_cell_value(1, 9)    # 获取第1行第25列数据  app_key
