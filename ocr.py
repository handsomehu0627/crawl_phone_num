import base64
import json

from PIL import Image
import pytesseract
import cv
import requests

'''
steps:
        #1 open  the image
        #2 through pytesseract

'''
def get_im():
    im = Image.open('/Users/jdd001/PycharmProjects/phone_num_check/media/screenshots/foo.png')
    print(im.size)
    im2 = im.crop((1580,600,1850,700))
    im2.save('/Users/jdd001/PycharmProjects/phone_num_check/media/img_findpwd.png')


def process_veriCode(uname, pwd, img):  # img represents image path
    with open(img, 'rb') as f:
        base64_data = base64.b64encode(f.read())
        b64 = base64_data.decode()
    data = {"username": uname, "password": pwd, "image": b64}
    result = json.loads(requests.post("http://api.ttshitu.com/base64", json=data).text)
    if result['success']:
        return result["data"]["result"]
    else:
        return result["message"]

if __name__ == '__main__':
    result = process_veriCode(uname='handsomehu', pwd='qwertyuiop12', img='/Users/jdd001/PycharmProjects/phone_num_check/media/img_findpwd.png')
    print(result)



