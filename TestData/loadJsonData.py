'''
Created on 2017年7月21日

@author: Administrator
'''

import json

class loadData():

    def loadUserName(self):
        f=open("..\TestData\loginName.json",encoding='utf-8')
        accout=json.load(f)
        f.close
        print(accout)
        print(accout[0])
        print(accout[1])
        print(accout[0]['loginname'])
        print(accout[0]['password'])
        return accout
        
        
        
if __name__ == '__main__':
    namdata=loadData();
    namdata.loadUserName()
    
        
 
        