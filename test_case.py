import unittest
import RA, RS, DI, RL, ASQ
import data


class Test_Speaking(unittest.TestCase):

    def test_Case_RA(self):
        text = RA.Test_RA(data.chrome, data.Url, data.ra)
        self.assertpy.assert_that(f'{text}').is_equal_to("点击彩色单词可查看解析")

    def test_Case_RS(self):
        text = RS.Test_RS(data.chrome, data.Url, data.rs)
        self.assertpy.assert_that(f'{text}').is_equal_to("点击彩色单词可查看解析")

    def test_Case_DI(self):
        text = DI.Test_DI(data.chrome, data.Url, data.di)
        self.assertpy.assert_that(f'{text}').is_equal_to("点击彩色单词可查看解析")

    def test_Case_RL(self):
        text = RL.Test_RL(data.chrome, data.Url, data.rl)
        self.assertpy.assert_that(f'{text}').is_equal_to("点击彩色单词可查看解析")

    def test_Case_ASQ(self):
        text = ASQ.Test_ASQ(data.chrome, data.Url, data.asq)
        self.assertpy.assert_that(f'{text}').is_equal_to("点击彩色单词可查看解析")


if __name__ == "__main__":
    unittest.main()


# (driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div/div[2]/div[3]/div/div[1]/button')).click()  # 关闭评分弹窗

# (driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[4]/div/div[10]/div[1]/button[2]')).click()  # 点击重做
# def redo(driver):
#     text = (driver.find_element_by_xpath('//*[@id="root"]/div[2]/div[4]/div/div[6]/div[2]/div[1]')).text()
#     a.assert_that(f'{text}').is_equal_to("点击开始录音")  # 断言重做成功

# (driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div[1]/div/div')).click()  # 点击评分弹窗
# text = (driver.find_element_by_xpath('/html/body/div[2]/div/div[2]/div/div/div/div[2]/div[4]/div[1]')).click()
# a.assert_that(f"{text}").is_equal_to("最新")