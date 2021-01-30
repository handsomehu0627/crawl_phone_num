# string = 'JSESSIONID=42F1B86458F0CACFDA7EB609B53E298F; acw_tc=debc08d616119759504408129e1431834e828c79a7a8c09de81d4d5f45; SERVERID=fc5216111c418f7ea18d4ede0d3c0bc0|1611975957|1611975950'
#
# var = string.replace(';', "','")
# var2 = var.replace('=', "':'")
# final = "'" + var2 + "'"
# print(final)
from selenium import webdriver
import time
'''

this script is for automatic-ly fetch the cookie

'''

driver = webdriver.Chrome()

driver.get(url='http://www.jszwfw.gov.cn/jsjis/front/accountCancel/inputUserMsg.do')
driver.find_element_by_id('accountnum').send_keys('36253119900902425X')
randcode = input('please enter the randcode:')
driver.find_element_by_xpath('//*[@id="randCode"]').send_keys(randcode)
driver.find_element_by_xpath('//*[@id="inputusermsgform"]/div/div[3]/input').click()
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