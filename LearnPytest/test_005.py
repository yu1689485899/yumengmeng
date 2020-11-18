'''
fixture 可以带参数和返回值
'''

import pytest


#  测试前置:准备测试数据,在测试用例中使用测试数据。测试数据使用fixture的返回值来表示


# @pytest.fixture()
# def username_pwd():
#     return {"username": "root", "pwd": 123456}  # 可以返回任意类型的
#
#
# def test_login(username_pwd):
#     print(f"测试数据为:{username_pwd['username']}")
#     # print("测试数据为:",{username_pwd['username']})
#
#
# # 相同的测试用例，只是每次输入的数据不同
# @pytest.fixture(params=['root', 'admin', 'administrator', '12323'])  # 多组用户名
# def data(request):  # request 时固定写法
#     return request.param  # request.param是固定写法，取到每一组数据
#
# #
# def register(data):
#     url = "http://jy001:8081/futureloan/mvc/api/member/register"
#     r = requests.post(url, data=data)
#     return r


@pytest.fixture(params=[{"casedata": 'root', "except": "成功"},
                        {"casedata": 'admin', "except": "失败"}])  # 多组用户名
def data1(request):  # request 时固定写法
    return request.param  # request.param是固定写法，取到每一组数据


def test_login2(data1):
    print(f"使用用户名{data1}测试登录功能")


def test_login3(data1):
    print(f"使用用户名{data1['casedata']}测试登录功能,预期结果为{data1['except']}")


#
from nose_parameterized.test import expect

# #
# def register(data):
#     url = "http://jy001:8081/futureloan/mvc/api/member/register"
#     r = requests.post(url, data=data)
#     return r


# @pytest.fixture(params=[
#     {"casedata": {"mobilephone": "137123456789", "pwd": "123456abc", "regname": "aaa"},
#      "except": {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}}])
# def data1(request):
#     return request.param

# @pytest.fixture(params=[{"casedata": {"mobilephone": "137123456789", "pwd": "123456abc", "regname": "aaa"},
#                          "except": {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}}])
# def data1(request):
#     return request.param
#
#
# def test_login4(data1):
# # print(f"使用手机号:{data1['casedata']}")
# # 测试步骤
# real = register(data1["casedata"])
# # # 检查结果
# assert real.json()['msg'] == data1["except"]["msg"]
# assert real.json()['code'] == data1["except"]['code']
# print([item[key] for item in data1 for key in item])
