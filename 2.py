from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

fo = open("e:/abc.txt","w")
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
driver = webdriver.Chrome(executable_path='E:/Program Files/chromedriver_win32/chromedriver', chrome_options=chrome_options)
driver.get("https://www.manhuadui.com/manhua/yirenzhixia/")
#time.sleep(3)
element = driver.find_element_by_id("chapter-list-1")
elements = element.find_elements_by_tag_name("li")
for i in elements:
    temp = i.find_elements_by_tag_name("a")
    a = temp[0]
    name = a.get_attribute("title")
    site = a.get_attribute("href")
    fo.write(name+";"+site+"\n")

#print(elements[2].text)
#elements = element.find_element_by_tag_name("li")
#for i in elements:
    #print(i)
fo.close()
driver.quit()
#os.system('taskkill /im chromedriver.exe /F')
#os.system('taskkill /im chrome.exe /F')
