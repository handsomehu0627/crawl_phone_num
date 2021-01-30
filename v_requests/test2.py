# class Bad(Exception):
#     print('no error')
#
#
# try:
#     print('hhhh')
#     raise Bad()
#     print('tag')
#
# finally:
#     print('ggg')
#     assert 1 < 0, print('error')
from selenium import webdriver
import time

# driver = webdriver.Chrome()
# driver.get(url='http://www.jszwfw.gov.cn/jsjis/front/accountCancel/inputUserMsg.do')
#
# driver.find_element_by_id('accountnum').send_keys('411424199605254259')
#
# randcode = input('please enter the randcode:')
# driver.find_element_by_xpath('//*[@id="randCode"]').send_keys(randcode)
#
# driver.find_element_by_xpath('//*[@id="inputusermsgform"]/div/div[3]/input').click()
# cookie1_raw = driver.get_cookies()
# cookie1 = [item["name"] + "=" + item["value"] for item in cookie1_raw]
# cookiestr = ';'.join(item for item in cookie1)
# string = cookiestr
# var = string.replace(';', "','")
# var2 = var.replace('=', "':'")
# final = "'" + var2 + "'"
# print(final)
driver = webdriver.Chrome()
        # step1. get the first cookie

driver.get(url='http://www.jszwfw.gov.cn/jsjis/front/accountCancel/inputUserMsg.do')
driver.find_element_by_id('accountnum').send_keys('411424199605254259')
randcode = input('please enter the randcode:')
driver.find_element_by_xpath('//*[@id="randCode"]').send_keys(randcode)
driver.find_element_by_xpath('//*[@id="inputusermsgform"]/div/div[3]/input').click()
        # cookie1_raw = driver.get_cookies()
        # # step1.2 transfer the raw cookie to the format that we need
        # cookie1 = [item["name"] + "=" + item["value"] for item in cookie1_raw]
        # cookiestr1 = ';'.join(item for item in cookie1)
        # string = cookiestr1
        # var = string.replace(';', "','")
        # var2 = var.replace('=', "':'")
        # final1 = "'" + var2 + "'"

        # step2. get the second cookie
time.sleep(2)
driver.find_element_by_xpath('//*[@id="username"]').send_keys('雷鹏')
driver.find_element_by_xpath('//*[@id="papers"]').send_keys('36253119900902425X')
driver.find_element_by_xpath('//*[@id="usermbile"]').send_keys('15295698722')
driver.find_element_by_xpath('//*[@id="inputusermsgform"]/div/div[4]/input').click()

cookie1_raw = driver.get_cookies()
driver.close()
# step1.2 transfer the raw cookie to the format that we need
cookie1 = [item["name"] + "=" + item["value"] for item in cookie1_raw]
cookiestr1 = ';'.join(item for item in cookie1)
string = cookiestr1
var = string.replace(';', "','")
var2 = var.replace('=', "':'")
final1 = "'" + var2 + "'"
print(final1)