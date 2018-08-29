#coding=utf-8
import pytest
from selenium import webdriver

def test_s1(browser=webdriver.Firefox):
    driver=browser
    driver.get("https://www.cnblogs.com/yoyoketang/")
    t=driver.title
    print(t)
    assert  t==u"test"


if __name__ == '__main__':
    pytest.main(["-s", "test_fix1.py"])