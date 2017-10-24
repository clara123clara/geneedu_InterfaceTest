'''
Created on 2017年10月24日

@author: Administrator
'''
import xlrd
import requests
import json
import re

class WebApiTest:
        
    # 请求主方法
    def request(self, rqtype, rqurl, paramete):
        self.rqurl = rqurl  # API地址
        self.rqtype = rqtype  # 请求类型get or post
        self.paramete = paramete  # 请求参数
        #self.headers = headers  # 请求头

        if rqtype == "get":
            apirqhttp = requests.get(url=rqurl, params=paramete)  # 发送请求
            code = apirqhttp.status_code  # 保存返回状态
            pam = apirqhttp.text  # 保存返回数据并将json转为dict
            head = apirqhttp.headers
            return code, pam,head
        if rqtype == "post":
            apirqhttp = requests.post(url=rqurl, data=paramete)
            code = apirqhttp.status_code
            pam = apirqhttp.text
            head = apirqhttp.headers
            return code, pam,head
        else:
            print("请求参数错误，请求类型只支持get+post，请求地址支持string，参数支持dict")
     
            
    # 获取登陆用户的cookies值
    def getcookies(self):
        rqtypes = "post"
        rqurls = "http://www.geneedu.cn/honeybee/passport/login/logon.do"
        parametes = {
        "returnUrl":"",
        "userVo.loginName":"chenjiajia",
        "userVo.password":"ac1e1f9138e18dcca01311bd10abecf5"
        }
        headers = None
        
        cod, pam ,head= WebApiTest().request(rqtypes, rqurls, parametes)  # 掉用request方法请求登录
        responPam = json.loads(pam)  # 保存返回数据并将json转为dict
        
        #print(cod)
        #print(responPam)
        #print(head)
        
        myCookies=head.get("Set-Cookie")
        
        p = '(?<=edustar_login_token=).+?(?=;)'
        pattern1 = re.compile(p)
        matcher1 = re.search(pattern1,myCookies)
        cookie1 = matcher1.group(0)
        #print('edustar_login_token=',cookie1)
        
         
        p = '(?<=sso_key=).+?(?=;)'
        pattern1 = re.compile(p)
        matcher1 = re.search(pattern1,myCookies)
        cookie2 = matcher1.group(0)
        #print('sso_key=',cookie2)
        
         
        p = '(?<=sso_token=).+?(?=;)'
        pattern1 = re.compile(p)
        matcher1 = re.search(pattern1,myCookies)
        cookie3 = matcher1.group(0)
        #print('sso_token=',cookie3)
     
        p = '(?<=JSESSIONID=).+?(?=;)'
        pattern1 = re.compile(p)
        matcher1 = re.search(pattern1,myCookies)
        cookie4 = matcher1.group(0)
        #print('JSESSIONID=',cookie4)  
        
        
        p = '(?<=ESessionID=).+?(?=;)'
        pattern1 = re.compile(p)
        matcher1 = re.search(pattern1,myCookies)
        cookie5 = matcher1.group(0)
        #print('JSESSIONID=',cookie4) 
        
        return cookie1,cookie2,cookie3,cookie4,cookie5
    
    #获取第一个sheet对象
    def xlsxSheet(self,xlsFile):
        xlsFile_obj=xlrd.open_workbook(xlsFile)
        sheetName=xlsFile_obj.sheet_names()[0] #获取第一个sheet名称
        sheet_obj=xlsFile_obj.sheet_by_name(sheetName)
        return sheet_obj
    
    

if __name__ == '__main__':
    my_apitest=WebApiTest()
    my_apitest.getcookies()
    
    fileUrl="Request_test_data.xlsx"
    
    sheetObj1=my_apitest.xlsxSheet(fileUrl)
    nrow=sheetObj1.nrows  #行总数
    ncols=sheetObj1.ncols #列总数
    col_data=sheetObj1.col_values(0) #获取第一列的数据
    row_data=sheetObj1.row_values(1) #获取第二行的数据
    
    #print("第一lie数据：",col_data)
    #print("第一行数据：",row_data)
    
    for i in range(1, nrow):  # 循环每行，并获取每行每列的值，因为第一行是标题，从第二行开始
        row_data = sheetObj1.row_values(i)  # 获取第i行的数据
         
        case_nums = int(row_data[0])  # 获取第i行的某个数据
        rqtypes = str(row_data[1])
        rqurls = str(row_data[2])
         
        a = row_data[3]  # 请求参数，并且一次取出这一行所有的参数
        #print("参数：",a)
        aa="{"+a+"}"
        json_a=json.loads(aa)
        print("用户登陆参数json_a对象：",json_a)

    

        access_token = my_apitest.getcookies()  # 获取token
        headers = {"Authorization": access_token}
        codetest, pamtest,head = my_apitest.request(rqtypes, rqurls, json_a)
        print ("用例编号：", case_nums, "code码：", codetest,'返回的head数据:',head)
        print ("返回参数：",pamtest)
        print("================================")
    
    
    
    
    
    
    
    
    
    
    