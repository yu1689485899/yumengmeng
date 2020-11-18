'''
发送get请求
'''
import requests

# 接口地址:"http://www.baidu.com"
# 发送一个get请求，r时收到的响应
r = requests.get("http://www.baidu.com")
# 文本格式的响应内容
print(r.text)
# 响应码
print(r.status_code)
assert r.status_code == 200
# ok
print(r.reason)
assert r.reason == 'OK'

# http://jy001:8081/futureloan/mvc/api/member/register

r = requests.get("http://jy001:8081/futureloan/mvc/api//loan/generateRepayments")
assert r.status_code == 200
assert r.reason == 'OK'
print(r.text)
assert r.json()['status'] == 1
print(777)
assert r.json()['code'] == '20403'
print(888)
# assert r.status_code ==
#
# print(r.reason)
# assert r.status_code == 'OK'

# get请求带参数
# 方法1：拼接到url后面
r = requests.get('http://jy001:8081/futureloan/mvc/api/member/register?mobilephone=')
# print(r.text)
assert r.status_code == 200
assert r.reason == 'OK'
print(r.text)
assert r.json()['code'] == '20103'
# 方法2：使用params传参数
url = "http://jy001:8081/futureloan/mvc/api/member/register"
canshu = {"mobilephone": "", "pwd": 123456, "regname": ""}
r = requests.get(url, params=canshu)
print(r.text)

# get请求带请求头,设置User - Agent伪装成浏览器发送的请求，避免服务器屏蔽自动化发的请求
url = "http://www.httpbin.org/get?mobilephone&pwd=123456&ragname=helloworld"
# 一个测试网站,get是接口名字，发送的请求原装返回来
r = requests.get(url)  # "User-Agent": "python-requests/2.24.0",
print(r.text)

# User-Agent 包含浏览器的版本号，操作系统的版本号
tou = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/85.0.4183.121 Safari/537.36"}
r = requests.get(url, headers=tou)
print(r.text)

url = "https://wenku.baidu.com/view/027d607deff9aef8941e06c0.html"
r = requests.get(url, headers=tou)
print(r.text)
print("蜂群算法源代码" in r.text)
