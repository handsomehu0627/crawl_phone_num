import requests
import re
import time
from selenium import webdriver

# login to the second page
session = requests.session()
session.headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) '
                  'Chrome/87.0.4280.141 Safari/537.36',
}
# cookie1 = {
#         'pageUrl':'http%3A%2F%2Fwww.jszwfw.gov.cn%2Fjsjis%2Ffront%2FaccountCancel%2FscanFace.do',' _pubk':'MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCb71WiUMr2WMwCvCJC%2FM868kojjC5nTlW2VAXw%0AWOaiPQh9F9pbs8MgoqUMeXEJb7H9LWh%2FYqtv8eTpRQq6TCMyaU8u%2Fvj5rZsqFR7wEOEL%2BzDdt7Xr%0A%2Fn7aoOwRDMYRPdnxV5PwyDLYrVGX4%2Fx4%2BSxcpbflgchjPHx10ubEd7KM2QIDAQAB%0A',' pageUrl':'http%3A%2F%2Fwww.jszwfw.gov.cn%2Fjsjis%2Ffront%2Flogin.do',' JSESSIONID':'232CC3D56D92A32833F8A66622091C6F',' _jubacdata':'715bfa6ab5ae268b354dc235bf5fd7160e155d2f6dc0aa3ae04c2954aa41a0840cfe599352c788436dfdf8f311cc1636f33d6f9130a23443cc308f7b9a8ef2df32c79d6e4e6a81d974e6cd60b1bd0ab024550b6db391e001a642b7616b1f4577ac983fa5f218ec6a991c815e0488ba6ff640c9c4517060f4',' acw_tc':'3ad79d1916119074505731706ec828d4c247604866c2506d816eb5eb87',' SERVERID':'bc38d539bdb4e9df6fbd88e7a47405f3|1611907546|1611907450'
#
# }
# session.get(url='http://www.jszwfw.gov.cn/jsjis/front/accountCancel/confirmUserMsg.do', cookies=cookie1)

# send post requests with form-data
cookie2 = {
        'JSESSIONID':'42F1B86458F0CACFDA7EB609B53E298F',' acw_tc':'debc08d616119759504408129e1431834e828c79a7a8c09de81d4d5f45',' SERVERID':'fc5216111c418f7ea18d4ede0d3c0bc0|1611975957|1611975950'

}

form_data = {
    'name': '雷鹏',
    'papersNumber': '36253119900902425X',
    'mobile': '15295698729',
}
res = session.post(url='http://www.jszwfw.gov.cn/jsjis/front/accountCancel/checkInfo.do', cookies = cookie2, data=form_data)
# res = session.post(url='http://www.jszwfw.gov.cn/jsjis/front/accountCancel/checkInfo.do', data=form_data)
print(res.text)
if res.text.__contains__('true'):
    print('该用户的电话号码是：')
    print('---------------------------all done!!! ---------------------------')




