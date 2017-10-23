'''
Created on 2017年7月19日

@author: Administrator
'''
import requests
import json
import unittest
import re
from TestData.loadJsonData import *

jsonData=loadData()
userAccount=jsonData.loadUserName()

class test_loginClass(unittest.TestCase):     #封装测试环境的初始化和还原的类  
    '''接口名称：用户登陆 '''
    def setUp(self):                 #放对数据可操作的代码，如对mysql、momgodb的初始化等,这里不对数据库进行操作！  
        print("start test")  
        pass  
    def tearDown(self):             #与setUp()相对  
        print("end test")  
        pass  
      
    def test_login(self,userName,userPasswd):
        ''' 循环测试用例 '''
        print("取数据测试每个测试用例")
        self.url="http://www.geneedu.cn/honeybee/passport/login/logon.do"
        self.header={"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8"}
        print(len(userAccount))
        self.data={
            "returnUrl":"",
            "userVo.loginName":userName,
            "userVo.password":userPasswd
            }
        self.r=requests.post(url=self.url, data=self.data)
        print(self.r.text)
        #正确反馈的json数据
        s=json.loads(self.r.text)
        responseData=s['data']['returnUrl']
        #self.assertIn("/honeybee/personcenter/index.do",self.r.text)
        print(userName)
        print(userPasswd)
        
    def test_do(self):    
        for i in range(len(userAccount)):
            print("现在的循环次数为：",i)
            aa=userAccount[i]['loginname']
            bb=userAccount[i]['password']
            a.test_login(aa,bb)
        print("打印完成")

        
     
        
if __name__ == '__main__':
    # unittest.main()
    #test_loginTest("setUp")
    aa={}
    bb={}
    a = test_loginClass()
    for i in range(len(userAccount)):
        print("现在的循环次数为：",i)
        aa=userAccount[i]['loginname']
        bb=userAccount[i]['password']
        a.test_login(aa,bb)
    print("打印完成")
    
        
        
        
        