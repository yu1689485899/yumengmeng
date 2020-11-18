import qq as qq
import requests

# r = requests.get("https://www.bagevent.com/account/dashboard")
from openpyxl.comments import author

# r = requests.get("https://www.bagevent.com/user/login")
# print(r.text)

head = {
    "cookies": "JSESSIONID=884274FF8E94BD71787973D029FC7DF9_gat"
               "=1Hm_lpvt_1fc37bec18db735c69ebe77d923b3ab9=1604737209 "
}

r = requests.get("https://www.bagevent.com/account/dashboard", headers=head)
print(r.text)
# # 没登陆时，title显示为<title></title>
# # 登陆后，title 显示为<title>百格活动 — 账户总览<title>
# '''
# requests中自动管理cookies的机制
# '''
# s = requests.session()  # 创建一个session，通过session 发送请求
# print("登陆之前的cookies", s.cookies)
# # 登录
# canshu = {
#     "access_type": 1,
#     "loginType": 1,
#     "emailLoginWay": 0,
#     "account": "2780487875@qq.com",
#     "password": "qq2780487875",
#     "remindmeBox": "on",
#     "remindme": 1
#
# }
#
# r = s.post("https://www.bagevent.com/user/login", data=canshu)
# print(r.text)
# print("登录之后的cookies", s.cookies)
# # # 调用dashboard的接口
# r = s.get("https://www.bagevent.com/account/dashboard")
# print("<title>百格活动 - 账户总览</title>" in r.text)
# # # 获取调查列表
#
# # # 查看某个调查的详细信息

# db = {"ip": "jy001", "port": 4406, "dbName": "future", "username": "root", "pwd": "123456"}
# print(db)