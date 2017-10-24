'''
Created on 2017年7月19日
主要完成登陆功能
@author: Administrator
'''

import requests
import json
import re

cookie1={}
cookie2={}
cookie3={}
cookie4={}


def test_login_rigth():
    url="http://www.geneedu.cn/honeybee/passport/login/logon.do"
   # header={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
    data={
        "returnUrl":"",
        "userVo.loginName":"test17",
        "userVo.password":"a3ccb3fb1802b5e3"
        }
    respon=requests.post(url=url,data=data)  #发送请求,返回post请求
    
    #print(requestsend.url)
    print('我的请求内容返回值为json格式：',respon.text)
    print('返回状态吗',respon.status_code)
    
    
    '''
    获取确定返回值中的测试对象
    '''
    #获取返回的json数据
    s=json.loads(respon.text)  #把json格式转换为python对象，字典对象
    #编码：把一个Python对象编码转换成Json字符串   json.dumps()
    #解码：把Json格式字符串解码转换成Python对象   json.loads()
    #loads对字符串，load是对句柄
    print(s.keys()) #打印字典的key值
    print(s['data'])
    print('获取字典中测valus:',s['data']['returnUrl'])
    print('---------------------------------')
    
    '''
            获取cookies,并通过正则表达式分别获取想要的值
    '''
    global myHeader,myCookies,cookie1,cookie2,cookie3,cookie4
    myHeader=respon.headers
    print('我的header是：',myHeader)
    #print("-------------------------")
    #print(a)
    myCookies=myHeader.get("Set-Cookie")
    print("我的Cookies:",myCookies)
    print('---------------------------------')
    
    p = '(?<=edustar_login_token=).+?(?=;)'
    pattern1 = re.compile(p)
    matcher1 = re.search(pattern1,myCookies)
    cookie1 = matcher1.group(0)
    print('edustar_login_token=',cookie1)
    
     
    p = '(?<=sso_key=).+?(?=;)'
    pattern1 = re.compile(p)
    matcher1 = re.search(pattern1,myCookies)
    cookie2 = matcher1.group(0)
    print('sso_key=',cookie2)
    
     
    p = '(?<=sso_token=).+?(?=;)'
    pattern1 = re.compile(p)
    matcher1 = re.search(pattern1,myCookies)
    cookie3 = matcher1.group(0)
    print('sso_token=',cookie3)
 
    p = '(?<=JSESSIONID=).+?(?=;)'
    pattern1 = re.compile(p)
    matcher1 = re.search(pattern1,myCookies)
    cookie4 = matcher1.group(0)
    print('JSESSIONID=',cookie4)   
    
    
if __name__ == '__main__':
    test_login_rigth()
    