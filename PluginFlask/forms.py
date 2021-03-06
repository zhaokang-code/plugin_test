#!/usr/bin/python
# coding=utf-8

from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, SelectField, RadioField
from wtforms.validators import DataRequired

# Flask是如何将表单渲染成HTML的？


class PluginForm(FlaskForm):
    """ 新闻表单 """
    page_location = StringField('', validators=[DataRequired("请输入..")],
        description="请输入标题",
        render_kw={"required": "required", "class": "form-control"})

    touch_show = TextAreaField('', validators=[DataRequired("请输入..")],
        description="请输入内容",
        render_kw={"required": "required", "class": "form-control"})

    image = StringField(label='新闻图片',
        description='请输入图片地址',
        render_kw={ 'class': 'form-control'})

    page_name = StringField('', validators=[DataRequired("请输入..")],
        description="请输入标题",
        render_kw={"required": "required", "class": "form-control"})

    sub_action = StringField('', validators=[DataRequired("请输入..")],
        description="请输入标题",
        render_kw={"required": "required", "class": "form-control"})

    prev_page_name = StringField('', validators=[DataRequired("请输入..")],
        description="请输入标题",
        render_kw={"required": "required", "class": "form-control"})



    submit = SubmitField('提交')



