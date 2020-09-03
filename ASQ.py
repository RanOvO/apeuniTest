from selenium import webdriver
from jpype import *
from time import sleep
from methodApi import login
from methodApi import speak
from methodApi import allow,score
import data


def Test_ASQ(Browser,Url,Qtype):

    ele=driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/button[2]')#选择语言
    ele.click()
    sleep(1)
    driver.get(Qtype)#进入题目
    allow() #允许录音
    speak(driver,1,30)#1是手点，2是自动录音&评分
    # score(driver,1)#手动点击录音&评分
    shutdownJVM()
    text = (driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[2]/div/div/div[4]/div')).text()
    return text
pass