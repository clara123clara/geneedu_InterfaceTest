'''
Created on 2017年7月19日

@author: Administrator
'''
import requests
import json
import unittest
import re
from subprocess import call


class test_loginTest(unittest.TestCase):     #封装测试环境的初始化和还原的类  
    '''接口名称：用户登陆 '''
    def setUp(self):                 #放对数据可操作的代码，如对mysql、momgodb的初始化等,这里不对数据库进行操作！  
        
        #初始化操作用户登陆url
        print("用例开始")
        self.url="http://www.geneedu.cn/honeybee/passport/login/logon.do"
        self.header={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}  
        #pass  
               
    def test_login_Name_right(self):
        ''' 测试用例：用户名和密码都正确'''
        self.url="http://www.geneedu.cn/honeybee/passport/login/logon.do"
        self.header={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
        self.data={
            "returnUrl":"",
            "userVo.loginName":"chenjiajia",
            "userVo.password":"ac1e1f9138e18dcca01311bd10abecf5"
            }
        self.r=requests.post(url=self.url, data=self.data)
        
        print(self.r.text)
        print(self.r.status_code)
        
        #正确反馈的json数据
        s=json.loads(self.r.text)
        responseData1=s['data']['returnUrl']
        responseData2=s['result']
        
        print('responseData1:',responseData1)
        print('responseData2:',responseData2)
        
        #断言数据是否正确
        self.assertEqual(self.r.status_code,200,'状态码错误')
        self.assertIn("/honeybee/personcenter/index.do",self.r.text)
        self.assertEqual(1,responseData2)
        
        print("=========================================================")
        
    def test_login_Name_error(self):
        '''用户名密码错误'''
        
        self.url="http://www.geneedu.cn/honeybee/passport/login/logon.do"
        self.header={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"} 

        self.data={
            "returnUrl":"",
            "userVo.loginName":"chenjiajia1",
            "userVo.password":"error"
            }
        self.r=requests.post(url=self.url, data=self.data)
        
        #正确反馈的json数据
        s=json.loads(self.r.text)
        #responseData1=s['data']['returnUrl']
        responseData2=s['result']
        print(self.r.text)
        print(self.r.status_code)
        
        #print('responseData1:',responseData1)
        print('responseData2:',responseData2)
        s=json.loads(self.r.text)
        responseData2=s['result']
        
        self.assertEqual(self.r.status_code,200,'状态码错误')
        self.assertNotIn("/honeybee/personcenter/index.do",self.r.text)
        self.assertNotEqual(responseData2,1)
        
    def test_login_name_password_empty(self):
        '''用户名密码为空'''
        
        self.url="http://www.geneedu.cn/honeybee/passport/login/logon.do"
        self.header={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"} 

        self.data={
            "returnUrl":"",
            "userVo.loginName":"",
            "userVo.password":""
            }
        self.r=requests.post(url=self.url, data=self.data)
        
        #正确反馈的json数据
        s=json.loads(self.r.text)
        responseData1=s['data']['tip']
        responseData2=s['result']
        print(self.r.text)
        print(self.r.status_code)
        
        print('responseData1:',responseData1)
        print('responseData2:',responseData2)
        s=json.loads(self.r.text)
        responseData2=s['result']
        
        self.assertEqual(self.r.status_code,200,'状态码错误')
        self.assertEqual(responseData1,"登录名或密码为空")
        self.assertNotEqual(responseData2,1)
         
            

        
             
    def tearDown(self):             #与setUp()相对  
        print("测试用例结束")  
        pass  
        
if __name__ == '__main__':
    # unittest.main()
    #test_loginTest("setUp")
    a = test_loginTest()
    a.test_login_Name_right()
    a.test_login_Name_error()
    a.test_login_name_password_empty()
    
    
       
        