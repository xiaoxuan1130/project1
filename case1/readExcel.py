#coding=utf-8
import requests
import unittest,ddt,time
import sys

reload(sys)
sys.setdefaultencoding('utf8')
class Test_api(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        url = "http://localhost/a/login"
        cls.s=requests.session()
        data = {
            'username': 'admin',
            'password': 'admin'
        }
        cls.s.post(url, data=data, verify=False)

    # def test_importImage(self):
    #     url="http://localhost/a/epipe/qiniu/upload/image"
    #     filepath="D:\haha.png"
    #     f={
    #         'files':('haha.png',open(filepath,'rb'),"image/png")
    #     }
    #     r=self.s.post(url,files=f)
    #     jpgurl=r.json()["url"]


    def test_importFile(self):
        url="http://localhost/a/input/eTenantPayDetails/import"
        filepath = "D:/software/20180828092250.xlsx"
        filename=unicode("20180828092250.xlsx","utf-8")
        filepath = unicode(filepath, "utf-8")
        # files={
        #     'file':(filepath,open(filepath,'rb'), 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        # }
        multiple_files={
            'file':(filename,open(filepath,'rb'),'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        }

        r=self.s.post(url,files=multiple_files)

if __name__ == '__main__':
    unittest.main()