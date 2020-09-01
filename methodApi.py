from jpype import *
from time import sleep
import data
def login(driver):
    print
    getDefaultJVMPath()
    startJVM(getDefaultJVMPath(), "-ea", r"-Djava.class.path=sikuli\sikulixapi.jar")
    java.lang.System.out.println("hello world")
    Screen = JClass("org.sikuli.script.Screen")
    screen = Screen()
    # screen.type(r"img\admin.png",data.deviluser)
    # sleep(1)
    # screen.type(r"img\pass.png",data.devilpsw)
    # sleep(1)
    # screen.click(r"img\3.png")

    # shutdownJVM()
    ele = driver.find_element_by_id('user_email')
    ele.send_keys(data.email)
    sleep(1)
    ele = driver.find_element_by_id('user_password')
    ele.send_keys(data.password)
    sleep(1)
    ele = driver.find_element_by_id('sign-in-btn')
    ele.click()
    return

def redio(driver):
    #DI://*[@id="root"]/div[2]/div[4]/div/div[5]/div[2]/div[3]/div/i
    ele=driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[4]/div/div[5]/div[2]/div[3]/div/i')# 开始录音
    ele.click()
    sleep(5)
    ele=driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[4]/div/div[5]/div[2]/div[3]/div/i')# 结束录音
    ele.click()
    sleep(1)
    return

def speak(driver,selecte,s):
    Screen = JClass("org.sikuli.script.Screen")
    screen = Screen()
    screen.click(r"img\red.png")  # 点击允许录音
    sleep(2)
    if selecte == 1:  # 手点
        redio(driver)
        sleep(1)
    else:  # 自动录音
        sleep(s)
    score(driver,1)
    return

def score(driver,type):
    Screen = JClass("org.sikuli.script.Screen")
    screen = Screen()
    if type == 1:
        ele = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[4]/div/div[8]/div[1]/button[1]')  # 提交
    elif type == 2:
        ele = driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[4]/div/div[8]/div[1]/button[1]')  # 提交
    ele.click()
    sleep(3)
    screen.click(r"img\pingfen.png")  # 点击评分
    if type == 2:
        sleep(1)
        ele=driver.find_element_by_xpath('/html/body/div[3]/div/div/ul/li[1]')
        ele.click()
    return

pass