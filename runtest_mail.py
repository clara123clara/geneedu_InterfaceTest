'''
Created on 2017年7月21日

@author: Administrator
'''

import unittest  
import requests  
import HTMLTestRunner  
import time  
import os  
import smtplib  
from email.mime.text import MIMEText  
from email.header import Header  
  
#======定义发送邮件========  
def send_mail(file_new):  
    f = open(file_new,'rb')  
    mail_body = f.read()  
    f.close()  
  
    msg = MIMEText(mail_body,'html','utf-8')  
    msg['Subject'] = Header('登陆接口自动化测试报告','utf-8')  
  
    smtp = smtplib.SMTP()  
    smtp.connect('smtp.chinaedustar.net')  
    smtp.login('yunwei@chinaedustar.net','gongdan@123')  
    smtp.sendmail('yunwei@chinaedustar.net','chenjiajia@chinaedustar.net',msg.as_string())  
    smtp.quit()  
    print('邮件已发出！注意查收。')  
  
#======查找测试目录，找到最新生成的测试报告======  
def new_report(test_report):  
    lists = os.listdir(test_report)  
    lists.sort(key=lambda fn:os.path.getmtime(test_report + '\\' + fn))  
    file_new = os.path.join(test_report,lists[-1])  
    print(file_new)  
    return file_new  
  
if __name__ == "__main__":  
    test_dir = "G:\\EclipseWorkspace\\IntaerfaceTest\\test_case"  
    test_report = "G:\\EclipseWorkspace\\IntaerfaceTest\\test_report"  
  
    discover = unittest.defaultTestLoader.discover(test_dir, pattern = 'test*.py')  
    #按照一定的格式获取当前的时间  
    now = time.strftime("%Y-%m-%d_%H-%M-%S-")  
  
    #定义报告存放路径  
    filename = test_report + "\\" + now + 'result.html'  
    fp = open(filename,'wb')  
    #定义测试报告  
    runner = HTMLTestRunner.HTMLTestRunner(stream =  fp, title = "xxx接口测试报告", description = "测试用例执行情况：")  
    #运行测试  
    runner.run(discover)  
    fp.close() #关闭报告文件  
  
    new_report = new_report(test_report)  
    send_mail(new_report) 
    
    