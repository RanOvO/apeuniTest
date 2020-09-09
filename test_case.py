
import unittest
import RA, RS, DI, RL, ASQ
import data
from selenium import webdriver
from methodApi import login
from assertpy import assert_that
from jpype import *

getDefaultJVMPath()
startJVM(getDefaultJVMPath(), "-ea", r"-Djava.class.path=sikuli\sikulixapi.jar")
java.lang.System.out.println("hello world")
class Test_Speaking(unittest.TestCase):

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_case1_RA(self):
        txt = RA.Test_RA(data.ra)
        print(f'{txt}')
        self.assertEqual("AI 语音识别:", f'{txt}')

    def test_case2_RS(self):
        txt = RS.Test_RS(data.rs)
        print(f'{txt}')
        self.assertEqual("AI 语音识别:", f'{txt}')

    # def test_case3_DI(self):
    #     txt = DI.Test_DI(data.di)
    #     print(f'{txt}')
    #     self.assertEqual("AI 语音识别:", f'{txt}')

    def test_case4_RL(self):
        txt = RL.Test_RL(data.rl)
        print(f'{txt}')
        self.assertEqual("AI 语音识别:", f'{txt}')

    def test_case5_ASQ(self):
        txt = ASQ.Test_ASQ(data.asq)
        print(f'{txt}')
        self.assertEqual("AI 语音识别:", f'{txt}')


if __name__ == "__main__":
    unittest.main()
shutdownJVM()


# (driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[3]/div/div[1]/button')).click()  # 关闭评分弹窗

# (driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[4]/div/div[10]/div[1]/button[2]')).click()  # 点击重做
# def redo(driver):
#     text = (driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[4]/div/div[6]/div[2]/div[1]')).text()
#     a.assert_that(f'{text}').is_equal_to("点击开始录音")  # 断言重做成功

# (driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div')).click()  # 点击评分弹窗
# text = (driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div[2]/div[4]/div[1]')).click()
# a.assert_that(f"{text}").is_equal_to("最新")