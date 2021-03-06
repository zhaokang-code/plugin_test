# coding:utf-8
import xlrd
from xlutils.copy import copy


class OperationExcel:
    def __init__(self, file_name=None, sheet_id=None):
        if file_name:
            self.file_name = file_name
            self.sheet_id = sheet_id
        else:
            self.file_name = '../dataconfig/HuaLin3.0_PluginTestReport.xls'
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
    print opers.get_cell_value(1, 7)    # 获取第2行第8列数据
    res = {"action_create_time": "1601368947862", "action_result":"","action_type":"common","app_key":"900","app_name":"美的美居","app_version":"6.8.1.3(prod)","device_brand":"apple","device_imei":"3CD31C2B-8DBB-4E6B-8BA2-1F62B8060048","device_resolution":"414X896","device_type":"iPhone12,1","identifier":"DA0F77AB-FB04-4271-9FCE-B56C444EFD25","install_way":"AppStore","iot_device_id":"145135535560333","load_duration":"1000","location_gps_lat":31.72475047452061,"location_gps_long":117.24448394775384,"network_operator":"46002","network_type":"WIFI","opt_system_type":"ios","opt_system_version":"13.7","page_id":"BD8A4789-B171-4ED8-AB37-EFC89204244A","page_name":"morePage","plugin_package":"T0xCA_001A0220","prev_page_name":"fridgeMainPage","sub_action":"quit_click","uid":"19be6a03fd5040c8a545c6a4b581165b","use_duration":"1000","user_account":"15055162563","widget_name":"Ref_BCD-318WTPZM(E)","widget_version":"2.3.0"}
    res = str(res)
    print opers.write_value(1, 7, res)
    # print opers.get_rows_data('case_001')
    # print opers.get_row_num('case_001')
    # print opers.get_cols_data(0)
    # print opers.get_row_values(0)


