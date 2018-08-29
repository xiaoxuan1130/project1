#coding:utf-8
import os
import ConfigParser

#获取当前工作空间路径
cur_path=os.path.dirname(os.path.realpath(__file__))
#获取配置文件路径
cfg_path=os.path.join(cur_path,"cfg.ini")
#读取配置文件
conf=ConfigParser.ConfigParser()
conf.read(cfg_path)


smtp_server=conf.get("email","smtp_server")
port=conf.get("email","port")
sender=conf.get("email","sender")
psw=conf.get("email","psw")
receiver=conf.get("email","receiver")