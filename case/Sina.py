# coding:utf-8
import requests
from bs4 import BeautifulSoup
import re

import sys

reload(sys)
sys.setdefaultencoding('utf8')

# 先打开登录首页，获取部分cookie
def login():
    url = "https://home.cnblogs.com/u/ms-uap/relation/followers"

    headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
               }  # get方法其它加个ser-Agent就可以了

    s = requests.session()
    r = s.get(url, headers=headers,verify=False)
    print s.cookies

    # 添加登录需要的两个cookie
    c = requests.cookies.RequestsCookieJar()

    c.set('.CNBlogsCookie', '43A0DE43EAF0EE25D667E898D8C2E915AF343D1B9E046FA6F324496D248340BF5CDC4F88E017F7A2E6FBB775D53220C4F34849BC8249483C4F771BBCDB0BCB38403A7BF46F993F713BAE0A703AF993D24E1C0D96')  # 填上面抓包内容
    c.set('.Cnblogs.AspNetCore.Cookies','CfDJ8FHXRRtkJWRFtU30nh_M9mDCozlk4STR6Jqgw4OaQcw3qCnCWlmDOrqOTZe0YI90M9U2kzRtIq_NjqWy3GvbeA7QB-ZV8SlMRjuIgyn6GeT9Wt4kcoRNwUc3hnOL_SN74gzx2CKJU4EaZcmohkW9HBe4CSgQrSEIs9R_gFvUzw4bhapvNxyPKkhn1sfxTNCZ4a2WEOG8pFmIfAfmp5w1UCtXgMI9d0oeJjThjOJ1r6p_jqniLpTl64xciR8ci2o9-EXtfdHLNrqMHsAxc9qFo5H1oWBUxAcmbxHVDUIMCN8n')  # 填上面抓包内容
    s.cookies.update(c)
    print s.cookies

    r1=s.get(url)
    soup=BeautifulSoup(r1.content,"html.parser")
    fensi=soup.find_all(class_="current_nav")
    content=fensi[0].text
    content=content.replace("\n", "").replace(" ","")
    num=re.findall(u'Ta的粉丝\((.+?)\)',content)
    print(num)

    total=int(int(num[0])/45)+1

    first_list=soup.find_all(class_="avatar_name")
    for i in first_list:
        name=i.string.replace("\n","").replace("","")
        print(name)
        with open("name.txt","a") as f:
            f.write(name.encode("utf-8"+"\n"))


def test():
    content=u'Ta的粉丝(6551)'
    content=re.findall(u'Ta的粉丝\((.+?)\)',content)
    print(content)

if __name__ == '__main__':
    login()



