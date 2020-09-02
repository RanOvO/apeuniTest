from selenium import webdriver
from jpype import *
from time import sleep
from methodApi import login
from methodApi import speak
from methodApi import allow
from methodApi import score
import data

driver = webdriver.Chrome(data.chrome)
driver.maximize_window()
driver.get(data.Url)

login(driver)#登陆
sleep(3)
ele=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/button[2]')#选择语言
ele.click()
sleep(1)
#---------------------------RA
driver.get(data.ra)#进入题目
allow()
speak(driver,1,80)#自动录音&评分


#---------------------------RS
driver.get(data.rs)#进入题目
speak(driver,1,32)#自动录音&评分


#---------------------------DI
driver.get(data.di)#进入题目
speak(driver,1,70)#自动录音&评分


#---------------------------RL
driver.get(data.rl)#进入题目
speak(driver,1,120)#自动录音&评分


#---------------------------ASQ
driver.get(data.asq)#进入题目
speak(driver,1,30)#1是手点，2是自动录音&评分


#---------------------------SWT
driver.get(data.swt)#进入题目
sleep(2)
ele=driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[4]/div/div[6]/div[1]/textarea')
ele.send_keys('zy is small pig')
sleep(2)
score(driver,2)#自动录音&评分

#---------------------------WE
driver.get(data.we)#进入题目
sleep(2)
ele=driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[4]/div/div[6]/div[1]/textarea')
ele.send_keys('zy is small pig')
sleep(2)
score(driver,2)#自动录音&评分

shutdownJVM()
pass