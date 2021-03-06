# coding:utf-8
import re

# 正则表达式测试

str = "### strat something end trat something1 end strat something2 end   ###"
str1 = 'topic = plugin_action, data = {"app_name":"","app_version":"6.9.0.68(sit)"}      topic = plugin_action, data = {"app_name":"","app_version":"6.9.0.68(sit)"}'


l=[]
begin=l.find('_')
end=l.rfind('_')
ss=l[begin+1:end]



str = "### strat something end trat something1 end strat something2 end   ###"
str1 = 'topic = plugin_action, data = {"app_name":"","app_version":"6.9.0.68(sit)"}      topic = plugin_action, data = {"app_name":"","app_version":"6.9.0.68(sit)"}'
#res = re.match('something',str).span()
#res  = re.findall(r'[{}](.*?)[}]', str1)
res1 = '{"widget_name":"Ref_BCD-598WKPZH","widget_version":"3.0.0","pageName":"HfridgeMainPage","actionType":"common","subAction":"frozenOn","action_result":"","prev_page_name":"mideaHomePage","operation":"burialPoint","use_duration":"1000","load_duration":"1000"}'

res2 = ' {"option":"","recordId":"8800acb7-229a-4b1e-83cf-a2ba8c48c89f","settings":[{"key":"location","value":{"address":"绱煶璺?,"longitude":"117.244415","city":"鍚堣偉甯?,"time":"2020-10-17T15:46:18","latitude":"31.724684"}}]}'
res3 = '{"applianceMFCode":"0000","fileName":"T_0000_CA_310A0958_3.lua","applianceType":"0xCA","sn8":"310A0958","version":"3","url":"http://midea-file-test.oss-cn-hangzhou.aliyuncs.com/900/T_0000_CA_310A0958_3.lua","md5":"35855d6b2c200f796acee6203929def1"}'
res = '{"code":0,"msg":null,"data":{"applianceMFCode":"0000","fileName":"T_0000_CA_310A0958_3.lua","applianceType":"0xCA","sn8":"310A0958","version":"3","url":"http://midea-file-test.oss-cn-hangzhou.aliyuncs.com/900/T_0000_CA_310A0958_3.lua","md5":"35855d6b2c200f796acee6203929def1"}'
print len(res1)
#print res


'''

result = re.findall(".strat(.*)end.*", str)
#result = re.findall(".*{(.*)}.*", str1)
print result
for x in result:
    print x



str1 = 'topic = plugin_action, data = {"app_name":"","app_version":"6.9.0.68(sit)"}XXXXXXXtopic = plugin_action, data = {"app_name":"","app_version":"6.9.0.68(sit)"}'
num = re.findall(r'[{](.*?)[}]', str1) 
num1 = re.findall(r'[topic = plugin_action,](.*?)[}]', str1) 
print num1
print type(num)
'''