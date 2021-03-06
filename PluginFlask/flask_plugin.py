#!/usr/bin/python
# coding=utf-8
import sys
import logging

if sys.getdefaultencoding() != 'utf-8':
    reload(sys)
    sys.setdefaultencoding('utf-8')
sys.path.append('D:/3_project/MaiDianTest')
from datetime import datetime
from flask import Flask, render_template, flash, redirect, url_for, abort, request, make_response
from forms import PluginForm
from flask_wtf import FlaskForm
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String, DateTime, Boolean
from main.MaidianDemoIOS import DemoM
import os
from werkzeug.utils import secure_filename
from report_maker import Report
from flask import send_file, send_from_directory


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:123456@127.0.0.1:3306/kangdata?charset=utf8'
app.config['SECRET_KEY'] = 'a random string'
db = SQLAlchemy(app)


class PluginTest(db.Model):
    """ 模型 """
    __tablename__ = 'plugintest'
    id = Column(Integer, primary_key=True)
    touch_show = Column(String(50))
    page_location = Column(String(50))
    page_name = Column(String(20))
    sub_action = Column(String(20))
    prev_page_name = Column(String(20))
    res = Column(String(2000), nullable=False)
    created_at = Column(DateTime)   

    def __repr__(self):
        return '<News %r>' % self.title


@app.route('/index2020/maidian-list-page1/', methods=('GET', 'POST'))
def maidian_list_page1():
    # 获取数据库中全部行的object，然后传到index中去
    maidian_list = PluginTest.query.all()
    return render_template("index2020/maidian-list-page1.html", maidian_list=maidian_list)


@app.route('/index2020/maidian-list-page2/', methods=('GET', 'POST'))
def maidian_list_page2():
    # 获取数据库中全部行的object，然后传到index中去
    maidian_list = PluginTest.query.all()
    return render_template("index2020/maidian-list-page2.html", maidian_list=maidian_list)


@app.route('/index/', methods=('GET', 'POST'))
def index1():
    # 获取数据库中全部行的object，然后传到index中去
    maidian_list = PluginTest.query.all()
    return render_template("index.html", maidian_list=maidian_list)



@app.route('/index2020/', methods=('GET', 'POST'))
def index2020():
    # 模板首页
    return render_template("index2020.html")


@app.route('/index2020/welcome/', methods=('GET', 'POST'))
def welcome():
    # 我的桌面
    return render_template("index2020/welcome.html")


@app.route('/index2020/question-list/', methods=('GET', 'POST'))
def question_list():
    # 问题列表
    maidian_list = PluginTest.query.all()
    return render_template("index2020/question-list.html", maidian_list=maidian_list)


@app.route('/add/', methods=('GET', 'POST'))
def add():
    # 将form中的文本框/下拉框内容传入到html页面中去
    form = PluginForm()
    demo = DemoM()
    demo.read()
    demo.str_to_dict()

    # 将上述下文本框/下拉框中的值提交到数据库
    if form.validate_on_submit():
        new_obj = PluginTest(
            page_location=form.page_location.data,
            touch_show=form.touch_show.data,
            page_name=form.page_name.data,
            sub_action=form.sub_action.data,
            prev_page_name=form.prev_page_name.data,
            created_at=datetime.now(),
            res=demo.find_str(form.page_name.data, form.sub_action.data, form.prev_page_name.data)
        )
        db.session.add(new_obj)
        db.session.commit()
        flash("添加成功")

        return redirect(url_for('maidian_list_page2'))
    return render_template("add.html", form=form)  # 删除res = res


@app.route('/update/<int:pk>',methods=('GET', 'POST'))
def update(pk):
    """ 获取埋点数据库表中第pk行的object(pk是如何从index传到这的)    """
    new_obj = PluginTest.query.get(pk)
    if not new_obj:
        return redirect(url_for('index'))
    form = PluginForm(obj=new_obj)
    demo = DemoM()
    demo.read()
    demo.str_to_dict()
    if form.validate_on_submit():
        # 将编辑页page_location文本框输入的内容赋给数据库该行的page_location项
        new_obj.page_location = form.page_location.data
        new_obj.touch_show = form.touch_show.data
        new_obj.page_name = form.page_name.data
        new_obj.sub_action = form.sub_action.data
        new_obj.prev_page_name = form.prev_page_name.data
        # 将编辑页选择的关键字传入到demo.find_str方法中执行，得到最新的res再传到数据库中该行
        new_obj.res = demo.find_str(new_obj.page_name, new_obj.sub_action, new_obj.prev_page_name)
        db.session.add(new_obj)
        db.session.commit()
        return redirect(url_for('maidian_list_page2'))
    return render_template("update.html", form=form)


@app.route('/single_search/<int:pk>', methods=('GET', 'POST'))
def single_search(pk):
    """ 获取埋点数据库表中第pk行的object """
    new_obj=PluginTest.query.get(pk)
    demo=DemoM()
    demo.read()
    demo.str_to_dict()
    # 将该行的埋点关键字再次执行一遍得到最新res提交到数据库中去
    new_obj.res=demo.find_str(new_obj.page_name, new_obj.sub_action, new_obj.prev_page_name)
    # db.session.add(new_obj)
    db.session.commit()
    return redirect(url_for('maidian_list_page2'))


@app.route('/batch_search',methods=('GET', 'POST'))
def batch_search():
    # 获取数据库中全部行的object/批量查询
    maidian_list = PluginTest.query.all()
    demo = DemoM()
    demo.read()
    demo.str_to_dict()
    for single_list in maidian_list:
        page_name = single_list.page_name
        sub_action = single_list.sub_action
        prev_page_name = single_list.prev_page_name
        # 将最新执行得到的res存储到数据库
        single_list.res = demo.find_str(page_name,sub_action,prev_page_name)
        # db.session.add(single_list)
        db.session.commit()
    return redirect(url_for('maidian_list_page2'))


@app.route('/delete/<int:pk>',methods=('GET', 'POST'))
def delete(pk):
    """ 删除是POST请求"""
    if request.method == 'GET':
        obj = PluginTest.query.get(pk)
        if obj is None:
            return 'no'
        data = db.session.query(PluginTest).get(pk)
        db.session.delete(data)
        db.session.commit()
        return redirect(url_for('maidian_list_page2'))
    return 'no'


@app.route('/upload/', methods=('GET','POST'))
def upload():
    # 上传埋点缓存文件
    if request.method == 'POST':
        f = request.files['file']
        basepath = os.path.dirname(__file__)  # 当前文件所在路径
        upload_path = os.path.join(basepath, '../dataconfig',secure_filename(f.filename))  # 注意：没有的文件夹一定要先创建，不然会提示没有该路径
        f.save(upload_path)
        return redirect(url_for('index1'))
    return render_template('index1.html')


@app.route('/report',methods=('GET','POST'))
def report():
    get = Report()
    # 将数据库中埋点数据导出到excel报告中
    get.write_to_excel()
    # 从指定路径下载测试报告
    name = 'HuaLin3.0_PluginTestReport.xls'
    file_name = "HuaLin3.0_PluginTestReport.xls"
    file_path = "D:/3_project/MaiDianTest/dataconfig"
    ROOT_FOLDER = os.path.join(file_path, file_name)
    response = make_response(
        send_file(filename_or_fp=ROOT_FOLDER, as_attachment=True))
    response.headers["Content-Disposition"] = "attachment; filename={};".format(file_name)
    return response
    return redirect(url_for('index'))





'''
    #获取数据库新增行的id，然后获取该行对应的res返回到前端页面
    #如果数据库无数据则返回“无”
    try:
        id = db.session.query(PluginTest).all()[-1].id
        res = db.session.query(PluginTest).get(id).res
        page_name = db.session.query(PluginTest).get(id).page_name
    except:
        res = '无！'
    return render_template("index1.html",form=form,res=res,page_name=page_name)
'''


if __name__ == '__main__':
    app.run(debug=True)


