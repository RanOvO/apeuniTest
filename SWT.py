from selenium import webdriver
from jpype import *
from time import sleep
from methodApi import login
from methodApi import score
import data

driver = webdriver.Chrome(data.chrome)
driver.maximize_window()
driver.get(data.devilUrlIn)

login(driver)#登陆
sleep(3)
ele=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/button[2]')#选择语言
ele.click()
sleep(1)
driver.get(data.swt)#进入题目
sleep(2)
# target = driver.find_element_by_xpath( '//*[@id="root"]/div[2]/div[4]/div/div[2]/div[2]/div/button')
# driver.execute_script("arguments[0].scrollIntoView();", target)  # 往下滑动
ele=driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[4]/div/div[6]/div[1]/textarea')
ele.send_keys('zy is small pig')
sleep(2)
score(driver,2)#自动录音&评分
shutdownJVM()
pass