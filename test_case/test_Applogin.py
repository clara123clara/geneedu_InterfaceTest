'''
Created on 2017年7月27日

@author: Administrator
'''

import unittest
import requests
import json
from test.test_importlib.util import case_insensitive_tests


class test_Applogin_class(unittest.TestCase):
    '''
          测试类
    '''
    def setUp(self):
        unittest.TestCase.setUp(self)
        
    def test_Applogin(self):
        '''
                         测试APP登陆
        '''
        self.url="http://yun.geneedu.cn/passport/login.do"
        self.data={
            "appId":1,
            "deviceType":1,
            "password":"",
            "userName":"",
            "versionNum":9
            }
        self.r=requests.post(url=self.url,data=self.data)
        print(self.r.text)
        
        s=json.loads(self.r.text)
        print(s['message'])
    
        
        if s['message'] == "用户名或密码错误!":
           print("测试通过")
        else:
           print("测试用例执行未通过！！！")
           
        
    def tearDown(self):
        unittest.TestCase.tearDown(self)  
        
        
if __name__ == '__main__':
    dengl=test_Applogin_class()
    dengl.test_Applogin()
     