# coding:utf-8
from util.operation_excelIOT import OperationExcel
import json

'''
1）从IOT后台导出包含埋点信息的excel表格
2）从excel中读取埋点关键字，并重新组建成需要的埋点写入测试报告
'''

class GetAllM:
    def __init__(self):
        self.opers = OperationExcel()
        # self.get = self.getM()

    def getM(self):
        list = []
        for i in range(1, self.opers.get_lines()):
            for j in range(0, 52):
                if self.opers.get_cell_value(0, j) == 'app_key':
                    x1 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'network_operator':
                    x2 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'opt_system_version':
                    x3 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'page_id':
                    x4 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'app_name':
                    x5 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'app_version':
                    x6 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'network_type':
                    x7 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'action_type':
                    x8 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'device_imei':
                    x9 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'iot_device_id':
                    x10 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'page_name':
                    x11 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'load_duration':
                    x12 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'opt_system_type':
                    x13 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'prev_page_name':
                    x14 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'install_way':
                    x15 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'user_account':
                    x16 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'sub_action':
                    x17 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'location_gps_long':
                    x18 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'identifier':
                    x19 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'uid':
                    x20 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'action_create_time':
                    x21 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'plugin_package':
                    x22 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'location_gps_lat':
                    x23 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'device_resolution':
                    x24 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'widget_version':
                    x25 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'action_result':
                    x26 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'widget_name':
                    x27 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'use_duration':
                    x28 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'device_type':
                    x29 = self.opers.get_cell_value(i, j)
                elif self.opers.get_cell_value(0, j) == 'device_brand':
                    x30 = self.opers.get_cell_value(i, j)
            res = {"app_key": x1, "network_operator": x2, "opt_system_version": x3, "page_id": x4, "app_name": x5, \
                 "app_version": x6, "network_type": x7, "action_type": x8, "device_imei": x9, "iot_device_id": x10,
                 "page_name": x11, \
                 "load_duration": x12, "opt_system_type": x13, "prev_page_name": x14, "install_way": x15,
                 "user_account": x16, \
                 "sub_action": x17, "location_gps_long": x18, "identifier": x19, "uid": x20, "action_create_time": x21,
                 "plugin_package": x22, \
                 "location_gps_lat": x23, "device_resolution": x24, "widget_version": x25, "action_result": x26,
                 "widget_name": x27, \
                 "use_duration": x28, "device_type": x29, "device_brand": x30}
            # print res
            list.append(res)
        return list
        # return json.dumps(list[0], ensure_ascii=False, sort_keys=True, indent=2)

    def find_str(self, a, b, c):
        list = self.getM()
        for i in list:
            if not i['page_name'] == a and i['sub_action'] == b and i['prev_page_name'] == c:
                continue
            else:
                res = json.dumps(i, ensure_ascii=False, sort_keys=True, indent=2)
                return res.replace(" ", "")


if __name__ == '__main__':
    get = GetAllM()
    print get.find_str('fridgeMainpage', 'materialadd_click', 'mideaHomePage')