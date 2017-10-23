'''
Created on 2017年10月20日

@author: Administrator
'''

import unittest
import HTMLTestRunner
import time

if __name__ == '__main__':
    
    #test_dir = "G:\\EclipseWorkspace\\IntaerfaceTest\\test_case"  
    test_report = ".\\test_report" 
    test_dir=".\\test_case"
    
    discover = unittest.defaultTestLoader.discover(test_dir, pattern='test_*.py')
    #执行测试用例，实例化TextTestRunner类
    runner=unittest.TextTestRunner()
 
    
    #按照一定的格式获取当前的时间   
    now = time.strftime("%Y-%m-%d %H_%M_%S")
    #定义报告存放路径     
    filename = test_report + "\\" + now + 'result.html'   
    fp = open(filename,"wb")
    #定义测试报告  
    runner = HTMLTestRunner.HTMLTestRunner(stream = fp,title = "登陆接口测试报告",description = '测试用例执行情况')
    
    #运行测试   
    #通过该类下面的discover()方法可自动更具测试目录test_dir匹配查找测试用例文件（test*.py），并将查找到的测试用例组装到测试套件，因此可以直接通过run()方法执行discover
    runner.run(discover)  
    fp.close()#关闭文件对象把数据写进磁盘      
