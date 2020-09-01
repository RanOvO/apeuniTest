from selenium import webdriver
from jpype import *
from time import sleep
from methodApi import login
from methodApi import speak
import data

driver = webdriver.Chrome(data.chrome)
driver.maximize_window()
driver.get(data.Url)

login(driver)#登陆
sleep(3)
ele=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/button[2]')#选择语言
ele.click()
sleep(1)
driver.get(data.di)#进入题目
# speak(driver,2,70)#自动录音&评分
speak(driver,1,1)#手动点击录音&评分
shutdownJVM()
pass