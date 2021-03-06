# -*- coding: utf-8 -*-
import sys
sys.path.append('D:/3_project/MaiDianTest')
import MySQLdb.cursors
import json
from util.operation_excel import OperationExcel

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
'''
#新建表
CREATE TABLE IF NOT EXISTS `runoob_tbl`(
   `runoob_id` INT UNSIGNED AUTO_INCREMENT,
   `runoob_title` VARCHAR(100) NOT NULL,
   `runoob_author` VARCHAR(40) NOT NULL,
   `submission_date` DATE,
   PRIMARY KEY ( `runoob_id` )
)ENGINE=InnoDB DEFAULT CHARSET=utf8;
'''



'''
sql = 'delete from plugintest1'         #清空表内容
sql = 'drop table plugintest3'          #删除表
                                        #在表中插入行
                                        #修改表的value值
sql = 'alter table plugintest1 modify column sub_action varchar(30)' #修改表字符串长度限制
sql = 'alter table plugintest1 rename to plugintest2'                #修改表名 
sql = 'alter table plugintest2 drop column sub_action'                         #删除列表字段
sql = 'alter table plugintest2 add column sub_action VARCHAR(20) DEFAULT NULL' #增加一个字段，默认为空
sql = 'alter table plugintest2 add column sub_action VARCHAR(20) NOT NULL'     #增加一个字段，默认非空
sql = 'alter table plugintest2 change column sub_action sub_action1 varchar(10)' #修改列名
sql = 'create table plugintest3  like plugintest2' #复制表结构/不含表数据
sql = 'insert into plugintest3 select * from plugintest2' #将表2数据复制到表3中去/前提是俩表结构相同/不一样如下
     INSERT INTO 新表(字段1,字段2,.......) SELECT 字段1,字段2,...... FROM 旧表
     #复制表结构和表数据????

'''


sql1 = 'alter table plugintest rename to plugintest1111'
sql2 = 'create table plugintest  like plugintest301'     # 只能复制表头  不能复制表内容
sql3 = 'INSERT INTO plugintest(touch_show,page_location,page_name,sub_action,prev_page_name) SELECT touch_show,page_location,page_name,sub_action,prev_page_name FROM plugintest301;'
sql = 'alter table plugintest1111 rename to plugintest2'

cur.execute(sql3)
# 添加数据时使用
conn.commit()
# 关闭数据库连接
conn.close()   






'''
mysqlIDE中查询语句：
SELECT touch_show FROM kangdata.plugintest where sub_action='page_view';
SELECT touch_show as '触发条件'FROM kangdata.plugintest where sub_action='page_view';
'''