from selenium import webdriver
from jpype import *
from time import sleep
from methodApi import login,score,single,speak
import data

driver = webdriver.Chrome(data.chrome)
driver.maximize_window()
driver.get(data.Url)

login(driver)#登陆
sleep(3)
ele=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/button[2]')#选择语言
ele.click()
sleep(1)
driver.get(data.single)#进入题目
single(driver)
score(driver,3)#选择并评分
shutdownJVM()
pass