#coding=utf8
import os,time
import unittest
import HTMLTestRunner
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

cur_path=os.path.dirname(os.path.realpath(__file__))

def add_case(caseName="case",rule="test*.py"):
    case_path=os.path.join(cur_path,caseName)
    #如果不存在则创建
    if not os.path.exists(case_path):os.mkdir(case_path)
    #定义discover方法
    discover=unittest.defaultTestLoader.discover( case_path, pattern=rule, top_level_dir=None)
    return discover

def run_case(all_case,reportName="report"):
    now=time.strftime("%Y_%m_%d_%H_%M_%S")
    #用例文件夹名称
    report_path=os.path.join(cur_path,reportName)
    if not os.path.exists(report_path):os.mkdir(report_path)
    #测试报告生成的文件
    report_file_path=os.path.join(report_path,now+"report.html")
    fp=open(report_file_path,"wb")
    runner=HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'李月轩的测试',description=u'就是测试一下的')
    runner.run(all_case)

def get_newly_report_file(report_path):
    #获取当前报告所在的目录
    lists=os.listdir(report_path)
    #根据最后修改日期将该目录下的所有文件排序
    lambda fn:os.path.getmtime(os.path.join(report_path,fn))
    lists.sort()
    report_file=os.path.join(report_path,lists[-1])
    return report_file


def get_report_file(report_path):
    lists=os.listdir(report_path)
    lists.sort(key=lambda fn:os.path.getmtime(os.path.join(report_path,fn)))##获取文件最后修改的时间
    report_file=os.path.join(report_path,lists[-1])
    return report_file

def send_mail(sender,psw,receiver,smtpserver,report_file,port):
    #获取邮件正文
    with open(report_file,"rb") as f:
        mail_body=f.read()
    #定义邮件内容
    msg=MIMEMultipart()
    body=MIMEText(mail_body,_subtype='html',_charset='utf-8')
    msg['Subject']=u'自动化测试报告'
    msg['from']=sender
    msg["to"]=psw
    msg.attach(body)
    #添加附件
    att=MIMEText(open(report_file,"rb").read(),'base64','utf-8')
    att["Content-Type"]="application/actet-stream"
    att["Content-Disposition"]='attachment;filename="report.html"'
    msg.attach(att)
    try:
        smtp=smtplib.SMTP_SSL(smtpserver,port)
    except:
        smtp=smtplib.SMTP()
        smtp.connect(smtpserver,port)
    smtp.login(sender,psw)
    smtp.sendmail(sender,receiver,msg.as_string())
    smtp.quit()

if __name__ == '__main__':
    all_case=add_case()
    run_case(all_case)
    report_path=os.path.join(cur_path,"report")
    new_path=get_report_file(report_path)

    from config import readConfig
    sender=readConfig.sender
    psw=readConfig.psw
    smtp_server=readConfig.smtp_server
    port=readConfig.port
    receiver=readConfig.receiver
    send_mail(sender, psw, receiver, smtp_server, new_path, port)
