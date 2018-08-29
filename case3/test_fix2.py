#coding=utf-8
import pytest

def test_s1(browser):
    driver=browser
    driver.get("https://www.cnblogs.com/yoyoketang/")
    t=driver.title
    print(t)
    assert u"test" in t
