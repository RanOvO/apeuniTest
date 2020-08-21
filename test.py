from jpype import *
import data
from selenium import webdriver
from time import sleep

driver = webdriver.Chrome(data.chrome)
driver.maximize_window()
driver.get(data.devilUrlIn)

# 需安装VCForPython27
# F:\JAVA\jre1.8\jre\bin\server\jvm.dll
print
getDefaultJVMPath()
startJVM(getDefaultJVMPath(), "-ea", r"-Djava.class.path=F:\sikuli\sikulixapi.jar")
java.lang.System.out.println("hello world")
Screen = JClass("org.sikuli.script.Screen")
screen = Screen()
# r"F:\python\test\webauto\img\chrome.png" 你截取桌面上chrome图标的图片路径
# screen.doubleClick(r"F:\python\test\webauto\img\5.png")
screen.type(r"F:\python\test\webauto\img\admin.png","apeuni")
sleep(2)
screen.type(r"F:\python\test\webauto\img\pass.png","apeSandbox")
sleep(2)
screen.click(r"F:\python\test\webauto\img\3.png")

shutdownJVM()
