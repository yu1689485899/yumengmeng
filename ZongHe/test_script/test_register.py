'''
注册的测试脚本
'''
import pytest
import requests

from ZongHe.baw import Member, DbOp
from ZongHe.caw import DataRead
from ZongHe.caw.BaseRequests import BaseRequests


# def register(data):
#     url = "http://jy001:8081/futureloan/mvc/api/member/register"
#     r = requests.post(url, data=data)
#     return r


# 注册失败
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_fail.yaml"))
def fail_data(request):  # 固定写法
    return request.param


# 注册成功
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_path.yaml"))
def path_data(request):  # 固定写法
    return request.param


# 重复注册
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_repeat.yaml"))
def repeat_data(request):  # 固定写法
    return request.param


# 注册失败
def test_register_fail(fail_data, url, baserequests):
    print(type(fail_data))
    print(f"测试数据为:{fail_data['casedata']}")
    print(f"预期结果为:{fail_data['except']}")
    r = Member.register(url, baserequests, fail_data['casedata'])
    print(r)
    assert r.json()['msg'] == fail_data['except']['msg']
    assert r.json()['status'] == fail_data['except']['status']
    assert r.json()['code'] == fail_data['except']['code']


# 注册成功
def test_register_pass(path_data, db, url, baserequests):
    print(f"测试数据为:{path_data['casedata']}")
    print(f"预期结果为:{path_data['except']}")
    phone = path_data['casedata']['mobilephone']
    # 初始化坏境，确保环境中没有影响本次执行的数据
    DbOp.deleteUser(db, phone)
    # 发送请求
    r = Member.register(url, baserequests, path_data['casedata'])
    #  1.检查响应结果
    assert r.json()['msg'] == path_data['except']['msg']
    assert r.json()['status'] == path_data['except']['status']
    assert r.json()['code'] == path_data['except']['code']
    #  2.检查实际有没有被注册(1.数据库;2.获取用户列表;3.用注册的用户登录)
    r = Member.getList(url, baserequests)
    print(r.text)
    assert phone in r.text
    # 清理环境，根据手机号删除注册用户
    DbOp.deleteUser(db, phone)


# 重复注册
def test_register_repeat(repeat_data, db, url, baserequests):
    print(f"测试数据为:{repeat_data['casedata']}")
    print(f"预期结果为:{repeat_data['except']}")
    phone = repeat_data['casedata']['mobilephone']
    #  初始化坏境，确保环境中没有影响本次执行的数据
    DbOp.deleteUser(db, phone)
    r = Member.register(url, baserequests, repeat_data['casedata'])
    assert r.json()['msg'] == repeat_data['except']['msg']
    assert r.json()['status'] == repeat_data['except']['status']
    assert r.json()['code'] == repeat_data['except']['code']
    r1 = Member.register(url, baserequests, repeat_data['casedata'])
    assert r1.json()['msg'] == '手机号码已被注册'
    # print(f"测试数据为:{repeat_data['casedata']}")
    # print(f"预期结果为:{repeat_data['except']}")
