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

    page_name = SelectField('page_name',
    choices=[('--请选择--', '--请选择--'),('morePage', 'morePage'),('smartCentrePage', 'smartCentrePage'),
    ('HfridgeMainPage','HfridgeMainPage'),
    ('smartScenePage','smartScenePage')],
        render_kw={'class': 'form-control'})

    sub_action = SelectField('sub_action',
    choices=[('--请选择--', '--请选择--'),('page_view', 'page_view'),('quit_click', 'quit_click'),
    ('tab_click','tab_click'),('refrigerator_click','refrigerator_click'),('refrigeratorChange','refrigeratorChange'),
    ('freezerTemperature','freezerTemperature'),('coolingOn','coolingOn'),
    ('coolingOff','coolingOff'),('frozenOn','frozenOn'),('frozenOff','frozenOff'),('more_click','more_click'),
    ('refresh button_click','refresh button_click'),('smartCentre_click','smartCentre_click'),
    ('smart scene_click','smart scene_click'),('smartOn','smartOn'),('smartOff','smartOff'),
    ('expiring','expiring'),('materialList','materialList'),('materialview_click','materialview_click'),
    ('materialadd_click','materialadd_click'),('voice_click','voice_click'),
    ('diet_click','diet_click'),('material_click','material_click'),('materialEncy_click','materialEncy_click'),
    ('menu_click','menu_click'),('more menu_click','more menu_click'),('hot menu_click','hot menu_click'),
    ('more hotmenu_click','more hotmenu_click'),('zucai_click','zucai_click'),('total menu_click','total menu_click'),
    ('dietary guidelines_click','dietary guidelines_click')],
        render_kw={'class': 'form-control'})

    prev_page_name = SelectField('prev_page_name',
    choices=[('--请选择--', '--请选择--'),('fridgeMainPage', 'fridgeMainPage'),
    ('mideaHomePage','mideaHomePage'),('HfridgeMainPage','HfridgeMainPage')],
        render_kw={'class': 'form-control'})

    submit = SubmitField('提交')



