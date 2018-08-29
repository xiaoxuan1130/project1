#coding:utf-8
import requests

def login2():
    url="http://localhost/a/login"
    url1 = "http://localhost/a/input/eTenantPayDetails/import/template"

    s=requests.session()
    data={
        'username':'admin',
        'password':'admin'
    }
    s.post(url,data=data,verify=False)
    print(s.cookies)

    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding": "gzip, deflate, sdch, br",
        "Accept-Language": "zh-CN,zh;q=0.8",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    }

    r = s.post(url1, headers=headers, verify=False)
    with open("yoyo.xls", "wb") as f:
        f.write(r.content)
    f.close()

def login1():
    url="http://localhost/a"
    headers={
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:44.0) Gecko/20100101 Firefox/44.0"
    }

    s=requests.session()
    r=s.get(url,headers=headers,verify=False)
    c=requests.cookies.RequestsCookieJar()

    url1="http://localhost/a/input/eTenantPayDetails/import/template"
    c.set('JSESSIONID','2ED2B1DCED91B06BB515B689A5838C6E')
    c.set('jeeplus.session.id','341819bf7fd048a88404d5c4f1455920')
    s.cookies.update(c)

    headers={
        "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
        "Accept-Encoding":"gzip, deflate, sdch, br",
        "Accept-Language":"zh-CN,zh;q=0.8",
        "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    }

    r=s.post(url1,headers=headers,verify=False)
    with open("yoyo.xls","wb") as f:
        f.write(r.content)
    f.close()

    print(s.cookies)

if __name__ == '__main__':
    login2()