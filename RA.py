from selenium import webdriver
from jpype import *
from time import sleep
from methodApi import login
from methodApi import speak
from methodApi import allow
# from methodApi import score
from selenium.webdriver.common.by import By
import data


def Test_RA(Qtype):

    driver = webdriver.Chrome(data.chrome)
    driver.maximize_window()
    driver.get(data.Url)
    login(driver)
    sleep(5)
    driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div[2]/div/div/div[2]/button[2]').click()
    #选择语言
    driver.get(Qtype)  # 进入题目
    sleep(5)
    allow()  # 允许录音
    speak(driver,1,80)  # 自动录音&评分
    # score(driver,1)  # 手动点击录音&评分

    sleep(20)
    ele = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[2]/div/div[2]/div[2]/div/div/div[3]/div[1]').text
    driver.quit()
    return ele

