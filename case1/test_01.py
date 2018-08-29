#coding=utf-8
import unittest
from common.TokenUtils import write_token
from common.TokenUtils import get_token
import requests

class Test_01(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        write_token("13684923393","lyx1130","http://192.168.3.166:8181/api/user/login")

    def test_01(self):
        url="http://192.168.3.166:8181/api/userCenter/getViewHistoryByPage"
        headers={
            'token':get_token()
        }
        result=requests.post(url,headers=headers)
        print(result)

if __name__ == '__main__':
    unittest.main()