#coding=utf-8
from selenium import webdriver
import os,io,yaml
from requests import get,post,Session
from common.logger import Log

class Blog():
    log=Log()

    def login(self):
        url="https://passport.cnblogs.com/user/signin"
        headers={
            "User-Agent":"Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
        }
        s=Session()
        r=s.get(url,headers=headers,verify=False)

        cookies={'.CNBlogsCookie':'43A0DE43EAF0EE25D667E898D8C2E915AF343D1B9E046FA6F324496D248340BF5CDC4F88E017F7A2E6FBB775D53220C4F34849BC8249483C4F771BBCDB0BCB38403A7BF46F993F713BAE0A703AF993D24E1C0D96',
                 '.Cnblogs.AspNetCore.Cookies': '=CfDJ8FHXRRtkJWRFtU30nh_M9mDCozlk4STR6Jqgw4OaQcw3qCnCWlmDOrqOTZe0YI90M9U2kzRtIq_NjqWy3GvbeA7QB-ZV8SlMRjuIgyn6GeT9Wt4kcoRNwUc3hnOL_SN74gzx2CKJU4EaZcmohkW9HBe4CSgQrSEIs9R_gFvUzw4bhapvNxyPKkhn1sfxTNCZ4a2WEOG8pFmIfAfmp5w1UCtXgMI9d0oeJjThjOJ1r6p_jqniLpTl64xciR8ci2o9-EXtfdHLNrqMHsAxc9qFo5H1oWBUxAcmbxHVDUIMCN8n'}
        url1="https://i.cnblogs.com/EditPosts.aspx?opt=1"
        body = {"__VIEWSTATE": "",
                "__VIEWSTATEGENERATOR": "FE27D343",
                "Editor$Edit$txbTitle": "这是3111",
                "Editor$Edit$EditorBody": "<p>这里111：http://www.cnblogs.com/yeki/</p>",
                "Editor$Edit$Advanced$ckbPublished": "on",
                "Editor$Edit$Advanced$chkDisplayHomePage": "on",
                "Editor$Edit$Advanced$chkComments": "on",
                "Editor$Edit$Advanced$chkMainSyndication": "on",
                "Editor$Edit$Advanced$txbEntryName": "",
                "Editor$Edit$Advanced$txbExcerpt": "",
                "Editor$Edit$Advanced$tbEnryPassword": "",
                "Editor$Edit$lkbDraft": "存为草稿",
                }

        r2=s.post(url1, headers=headers, verify=False,data=body)
        self.log.info(u'保存数据成功,保存后的地址为：%s'%r2)
        # 第三步：正则提取需要的参数值
        import re
        postid = re.findall(r"postid=(.+?)&", r2.url)
        # 提取为字符串
        self.log.info(u'需要删除的字段id为:%s'%postid )

        ##删除
        url3="https://i.cnblogs.com/post/delete"
        json3={"postId":postid[0]}
        r3=s.post(url3,headers=headers,verify=False,json=json3)
        self.log.info("删除后的结果为：%s"%r3.json())



