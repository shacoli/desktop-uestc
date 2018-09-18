import requests
import re
import time

c = time.time()

print("login test is beginning")

def login_test(account, password):
    session = requests.session()       #创建session对象
    #第一次 发送get请求 
    get = session.get("http://idas.uestc.edu.cn/authserver/login?service=http%3A%2F%2Fportal.uestc.edu.cn%2F")
    ITlist=re.findall(r'LT-(.+?)-cas',get.text)
    IT="LT-"+ITlist[0]+"-cas" #取得验证口令
    postdata = {
            'username': account,
            'password':  password,
            'lt': IT,
            'dllt':'userNamePasswordLogin',
            'execution':'e1s1',
            '_eventId':'submit',
            'rmShown':'1'
            }
    session.post("http://idas.uestc.edu.cn/authserver/login?service=http://portal.uestc.edu.cn/index.portal",data=postdata)
    a = session.get("http://eams.uestc.edu.cn/eams/home.action")

    #print(a)#<Response [200]>
    session.get("http://eams.uestc.edu.cn/eams/logout.action?jsdEkingstar=1&redirect=http%3A%2F%2Fportal.uestc.edu.cn%2Flogout.portal")
    return 0

