#-*-  coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import urllib.request
import os
import time


chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path='E:/Program Files/chromedriver_win32/chromedriver', chrome_options=chrome_options)
driver.implicitly_wait(3)
file = open("e:/abc.txt", "r")
try:
    la = file.readlines()

    for i in range(len(la)):
        two = la[i].rstrip().split(";")
        name = two[0]
        address = two[1]
        path = "e:/321/"+name
        print("正在抓取:"+name)
        if not os.path.exists(path):
            os.makedirs(path)
        driver.get(address)
        source = driver.page_source
        if "chapterImages" in source:
            a = driver.execute_script("return chapterImages")
            obj = driver.execute_script("return chapterPath")
            for s in range(len(a)):
                z = str(s + 1)
                if "http" in a[s]:
                    urllib.request.urlretrieve(a[s], path + "/" + z + ".jpg")
                else:
                    print("https://mhcdn.manhuazj.com/"+obj+a[s])
                    urllib.request.urlretrieve("https://mhcdn.manhuazj.com/"+obj+a[s], path + "/" + z + ".jpg")
                time.sleep(0.5)
        else:
            print("失败")
        time.sleep(2)
except Exception as err:
    print(err)
finally:
    file.close()
    driver.quit()
