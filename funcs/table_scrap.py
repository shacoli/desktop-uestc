# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 22:12:10 2018

@author: shacoli
"""
'''
1.更新优化了处理数据的方式，用正则表达式找到关键字'\r\n    table0\WmarshalTable\(' 
并标记前驱后驱位置，删去了之前分两次查找
2.大大提高了速度
'''
from bs4 import BeautifulSoup
import requests
import re
import time

c = time.time()
account = 2017030102012
password = "402561" # 全都强制转换字符串形式
################################################定义了课这一类########################################################
#class ClassType():
#     __slots__ = ['class_teacher', 'class_name','class_place','class_ninfos','class_id','class_time']
#     def __init__(self, class_teacher, class_name, class_place, class_ninfos, class_id, class_time):
#         self.class_teacher = class_teacher
#         self.class_name = class_name
#         self.class_place = class_place
#         self.class_ninfos = class_ninfos
#         self.class_id = class_id
#         self.class_time = class_time
    
################################################爬取学校网站课表###################################################
def Search_The_Table(account, password):
    print("欢迎使用新一代自助课表查询软件")
    #headers1 = {"User-Agent": 'Mozilla/5.0(WindowsNT10.0;Win64;x64) AppleWebKit/537.36(KHTML,likeGecko)
    #Chrome/63.0.3239.132Safari/537.36'}
    session = requests.session()       #创建session对象
    #第一次 发送get请求 
    get = session.get("http://idas.uestc.edu.cn/authserver/login?service=http%3A%2F%2Fportal.uestc.edu.cn%2F")
    ITlist=re.findall(r'LT-(.+?)-cas',get.text)
    IT="LT-"+ITlist[0]+"-cas"
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
    session.get("http://eams.uestc.edu.cn/eams/home.action")
    search_for_ids = session.get("http://eams.uestc.edu.cn/eams/courseTableForStd.action")
    #print(search_for_ids.text)
    ids=(((re.search(r'("[0-9]{6}")',search_for_ids.text)[0]).split("\"")))[1]
    data1={ 'ignoreHead':1,
        'setting.kind':'std', #同样 有班级课表
        'startWeek':1,
        'semester.id':203,  #将来要改 每个时间段不同
        'ids': ids}
    course=session.post("http://eams.uestc.edu.cn/eams/courseTableForStd!courseTable.action",data=data1).text
    global soup
    soup=BeautifulSoup(course,"html.parser")
    #print(soup)
    #########################################在这里使用正则表达式来处理课表########################################
    class_blocks = re.finditer(r'TaskActivity\(',str(soup)) #找到所有课开始的地方并生成一个迭代器
    end_class = re.search(r';\r\n    table0\WmarshalTable\(',str(soup))  #找到最后一节课的末尾位置
    start_number = []#申明一个可以存放TaskActivity\(的开始下标记的列表
    end_number = []#申明一个可以存放TaskActivity\(的结束下标记的列表
    for i in class_blocks:#开始迭代
        #print(i.span())#显示生成位置
        start_number.append(i.span()[0])#将分别开始的地点分别存入列表
        end_number.append(i.span()[1])#将分别结束的地点分别存入列表
    start_number.append(end_class.start())#将最后结束的地点分别存入列表
    #print(start_number)
    #print(end_number)  #分别打印出来看一看
    class_info_1 = [] #申明一个空列表来储存课堂信息第一部分
    class_info_2 = [] #申明一个空列表来储存课堂信息第一部分之后的所有部分
    for i in range(len(start_number)-1): #开始了用循环处理每一节课的信息
        single_class = str(soup)[end_number[i]:start_number[i+1]]
        #print(single_class)
        single_class_process_1 = single_class.split(";") #先通过分号对包含一整节课信息的字符串进行分割
        #print(single_class_process_1)
        class_info_1.append(single_class_process_1[0].split("\""))
        temp_info_2 = []
        for x in single_class_process_1[1:-1]:
            temp_info_2.append(x)
        class_info_2.append(temp_info_2)
    #print(class_info_2)
    class_info_1_process_2 = [] #声明一个空列表来存放整理过后的所有课程信息（除了每日上课具体时间）
    for i in range(len(class_info_1)):
        temp_class_info_1_process_2 = []#声明一个暂时性空列表来存放整理过后的临时单节课课程信息
        for x in [3,7,11,13]: #将每一个必要属性存入列表
            temp_class_info_1_process_2.append(class_info_1[i][x])#将每一个必要属性存入暂时性列表
        class_info_1_process_2.append(temp_class_info_1_process_2)#将暂时性单节课列表加入主列表
    #print(class_info_1_process_2)#检验一下
    for i in range(len(class_info_1_process_2)):     
         #将课代号复制成为每节课属性的第5项
        class_info_1_process_2[i].append(((class_info_1_process_2[i])[1])[-13:])
         #将课的名称孤立出来
        (class_info_1_process_2[i])[1] = ((class_info_1_process_2[i])[1])[:-13]
    for i in range(len(class_info_1_process_2)):   #将课的具体时间赋值到课程列表的第6，7，8....个属性
        temp_class_time = []
        for k in range(0,len(class_info_2[i]),2):
            if len(class_info_2[i][k]) == 35:
                temp_class_time.append([int(class_info_2[i][k][21])\
             ,int(class_info_2[i][k][33])*10+int(class_info_2[i][k][34])])
            else:
                temp_class_time.append([int(class_info_2[i][k][21]),int(class_info_2[i][k][33])])
        class_info_1_process_2[i].append(tuple(temp_class_time))
    print(class_info_1_process_2)

    session.get("http://eams.uestc.edu.cn/eams/logout.action?jsdEkingstar=1&redirect=http%3A%2F%2Fportal.uestc.edu.cn%2Flogout.portal")

Search_The_Table(account, password)
print(time.time()-c)
