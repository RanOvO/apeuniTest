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
    screen.type(r"img\admin.png",data.deviluser)
    sleep(1)
    screen.type(r"img\pass.png",data.devilpsw)
    sleep(1)
    screen.click(r"img\3.png")

    ele = driver.find_element_by_id('user_email')
    ele.send_keys(data.email)
    sleep(1)
    ele = driver.find_element_by_id('user_password')
    ele.send_keys(data.password)
    sleep(1)
    ele = driver.find_element_by_id('sign-in-btn')
    ele.click()
    sleep(3)
    return

def redio(driver):
    #DI://*[@id="root"]/div[2]/div[4]/div/div[5]/div[2]/div[3]/div/i
    ele=driver.find_element_by_xpath(data.startR)# 开始录音
    ele.click()
    sleep(10)
    ele=driver.find_element_by_xpath(data.endR)# 结束录音
    ele.click()
    sleep(1)
    return

def allow():
    Screen = JClass("org.sikuli.script.Screen")
    screen = Screen()
    screen.click(r"img\red.png")  # 点击允许录音
    return

def speak(driver,selecte,s):
    sleep(2)
    if selecte == 1:  # 手点
        redio(driver)
        sleep(2)
    else:  # 自动录音
        sleep(s)
    score(driver,1)
    return

def single(driver):
    ele=driver.find_element_by_css_selector(data.singleAnswer)
    ele.click()
    return

def double(driver):
    ele=driver.find_element_by_css_selector(data.doubleAnswer1)
    ele.click()
    ele=driver.find_element_by_css_selector(data.doubleAnswer2)
    ele.click()
    return

def score(driver,type):
    Screen = JClass("org.sikuli.script.Screen")
    screen = Screen()
    if type == 1 or type == 3 or type == 4:
        ele = driver.find_element_by_css_selector(data.submit)  # 提交
    elif type == 2:
        # ele = driver.find_element_by_xpath(data.submit)  # 提交
        ele=driver.find_element_by_css_selector(data.submit)
    ele.click()
    sleep(15)  #需要显示等待到提交成功

    #口语和写作
    if type ==1 or type ==2:
        screen.click(r"img\pingfen.png")# 点击评分
        # sleep(15)
    #     screen.click(r"img\close.png")# 关闭评分框

    # if type == 1:
    #     screen.click(r"img\delete.png")# 删除
    #     sleep(1)
    #     ele = driver.find_element_by_xpath(data.delete)
    #     ele.click()
    #     sleep(1)

    if type == 2:
        sleep(1)
        ele=driver.find_element_by_xpath('/html/body/div[3]/div/div/ul/li[1]')
        ele.click()
    return


pass