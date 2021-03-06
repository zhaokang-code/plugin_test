# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String, DateTime, Boolean
import datetime

#ORM连接数据库
engine = create_engine("mysql://root:123456@127.0.0.1:3306/kangdata?charset=utf8")
#相当于MYsqldb中的游标cursor
Session = sessionmaker(bind=engine)
#ORM中基类对象
Base = declarative_base()

'''
ORM的几个主要实现：1）SqlObject 2）peewee 3）Django's ORM 4）SQLAlchemy
create_engine:连接数据库
本节：通过ORM建表，增删改查
ORM技术特点： 
    1.提高了开发效率。由于ORM可以自动对Entity对象与数据库中的Table进行字段与属性的映射，所以我们实际可能已经不需要一个专用的、庞大的数据访问层。 
    2.ORM提供了对数据库的映射，不用sql直接编码，能够像操作对象一样从数据库获取数据。 
ORM的优缺点： 
    1.ORM的缺点是会牺牲程序的执行效率和会固定思维模式。 
    2.从系统结构上来看,采用ORM的系统一般都是多层系统，系统的层次多了，效率就会降低。ORM是一种完全的面向对象的做法，而面向对象的做法也会对性能产生一定的影响。 

'''


class PluginTest(Base):
    ''' 在手动建的数据库中新建表 新闻类型 
    1）对于数据库中已经存在的表，可以自动生成该表的ORM模型类，只要：pip install sqlacodegen
    2）在cmd窗口输入以下命令生成模型：
       sqlacodegen --outfile=code.py mysql+pymysql://root:mysql@IP/数据库名称?charset=utf8 
       code.py 需要自己创建，root:mysql 对应数据库用户和密码 然后是数据库IP+数据库名称等配置。
    3)反之，新建好ORM模型后也可以自动生成对应的表。                       
    '''
    __tablename__ = 'plugintest1'
    id = Column(Integer, primary_key=True)
    touch_show = Column(String(50))
    page_location = Column(String(50))
    page_name = Column(String(30))
    sub_action = Column(String(20))
    prev_page_name = Column(String(20))
    res = Column(String(2000))
    created_at = Column(DateTime)
    # is_valid = Column(Boolean)


class MysqlOrmTest(object):

    # 对新建的表进行操作
    def __init__(self):
        self.session = Session()

    def add_one(self):
        ''' 添加数据 可以同时添加多条：使用self.session.add_all()方法'''
        k='dietary guidelines_click'
        new_obj = PluginTest(page_name=k,sub_action='动作',res = 'result',prev_page_name='前页面',
            created_at= datetime.datetime.now()
        )   
        self.session.add(new_obj)
        self.session.commit()
        return new_obj

    def get_one(self):
        ''' 获取一条数据   以下代表获取表中的第XX条数据 '''
        # return self.session.query(PluginTest).get(15)
        # return self.session.query(PluginTest).all()
        # 获取最后一行数据的行id
        data = self.session.query(PluginTest).all()[-1].id
        return data

    def get_more(self):
        ''' 获取多条数据 is_valid=1代表没有被删除的数据 0代表被删除的数据 '''
        # return self.session.query(News).filter_by(is_valid=1)
        # return self.session.query(PluginTest).filter_by(res = '')

    def update_data(self,pk):
        ''' 修改一条数据 '''
        obj = self.session.query(PluginTest).get(pk)
        print obj
        if obj: 
            # 修改is_valid为0
            obj.is_valid = 0
            self.session.add(obj)
            self.session.commit()
            return True
        return False

    def update_double(self):
        '''修改多条数据'''
        pass

    def delete_data(self):
        ''' 删除数据 '''
        # 获取要删除的数据
        data = self.session.query(PluginTest).get(68)
        self.session.delete(data)
        self.session.commit()


def main():
    # （一）通过ORM模型在数据库中新建表
    pro = PluginTest()
    pro.metadata.create_all(engine)
    # （二）添加一条数据到表中
    obj = MysqlOrmTest()
    rest = obj.add_one()
    # print dir(rest.id)
    # （三）获取一条查询信息
    # print obj.get_one().page_name
    # print obj.get_one()
    '''
    #（四）获取多条查询信息及条数
    print obj.get_more()
    #print obj.get_more().count()
    #for row in obj.get_more():
        #print row.id
    '''
    # （五）修改数据
    # print obj.update_data(1)
    # （六）删除数据
    # obj.delete_data()


if __name__ == '__main__':
    main()