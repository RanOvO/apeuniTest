from selenium import webdriver
from jpype import *
from time import sleep
import data
driver = webdriver.Chrome(data.chrome)
driver.get(data.releaseUrlUp)
ele = driver.find_element_by_id('user_nickname')
ele.send_keys(data.email)
sleep(1)
ele = driver.find_element_by_id('user_email')
ele.send_keys(data.email)
sleep(1)
ele=driver.find_element_by_id('user_password')
ele.send_keys(data.password)
sleep(1)
ele=driver.find_element_by_name('commit')
ele.click()
pass