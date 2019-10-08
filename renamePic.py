#-*-  coding:utf-8 -*-
import os
import shutil

os.chdir("e:/123")
#print(os.getcwd())
list = os.listdir()
for i in list:
    os.chdir("e:/123/"+i)
    picList = os.listdir()
    for j in picList:
        shutil.copy("e:/123/"+i+"/"+j, "e:/zxc")
        oldName = os.path.join("e:/zxc",j)
        newName = os.path.join("e:/zxc",i+"_"+j)
        try:
            os.rename(oldName,newName)
        except Exception as err:
            print(err)

