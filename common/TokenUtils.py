import os,io
import requests,json
from ruamel import yaml

curPath=os.path.dirname(os.path.realpath(__file__))

def get_token(yamlName="token.yaml"):
    file_path=os.path.join(curPath,yamlName)
    f=open(file_path)
    a=f.read()
    t=yaml.load(a)
    f.close()
    return t["token"]


def write_token(accountName,password,url):
    yamlName = "token.yaml"
    file_path=os.path.join(curPath,yamlName)
    payload={
        'account':accountName,
        'password':password
    }
    r=requests.post(url,data=payload)
    content=r.text
    contentPython=json.loads(content)
    dataList=contentPython.get("h")
    if(dataList.get("code")==200):
        dataResult=contentPython.get("b")
        token=dataResult.get("token")
        t={"token":token}
        with io.open(file_path, "w", encoding="utf-8") as f:
            yaml.dump(t, f, Dumper=yaml.RoundTripDumper)


