'''
Created on 2017年10月19日

@author: Administrator
'''
import unittest
from test_case.test_login_testcases import test_loginTest

if __name__ == '__main__':
    
   suite=unittest.TestSuite() #实例化  （实例化测试套件）
   
   suite.addTest(test_loginTest('test_login_Name_right')) #将测试用例加载到测试套件中，执行顺序是安装加载顺序
   suite.addTest(test_loginTest('test_login_Name_error'))
   
   #执行测试用例，实例化TextTestRunner类
   runner=unittest.TextTestRunner()
   runner.run(suite) #使用run()方法运行测试套件（即运行测试套件中的所有用例）



