#-*-  coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests

html = requests.get('https://www.dongmanhuayuan.com/search/%E5%8A%A8%E6%BC%AB%E5%9B%BD%20%E9%AD%94%E5%AF%BC%E5%B0%91%E5%B9%B4/1.html').text
soup = BeautifulSoup(html,'html.parser')
list = soup.select(".uk-text-break")
fo = open("e:/ft.txt","w")
for i in list:
    son = requests.get('https://www.dongmanhuayuan.com'+i.attrs["href"]).text
    sonSoup = BeautifulSoup(son,'html.parser')
    fo.write(i.text + ";" + sonSoup.select("#magnet_one")[0].attrs["value"] + "\n")
fo.close()
