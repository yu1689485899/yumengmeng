import pytest

from ZongHe.baw import DbOp, Member
from ZongHe.caw import DataRead


# 注册成功
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/register_path.yaml"))
def path_data(request):  # 固定写法
    return request.param


# 登录成功
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_pass.yaml"))
def path_data1(request):  # 固定写法
    return request.param


# 登录失败
@pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_faila.yaml"))
def path_data2(request):  # 固定写法
    return request.param


# 验证注册成功
def test_register_pass(path_data, db, url, baserequests):
    print(f"测试数据为:{path_data['casedata']}")
    print(f"预期结果为:{path_data['except']}")
    phone = path_data['casedata']['mobilephone']
    # 初始化坏境，确保环境中没有影响本次执行的数据
    DbOp.deleteUser(db, phone)
    r = Member.register(url, baserequests, path_data['casedata'])
    #  1.检查响应结果
    assert r.json()['msg'] == path_data['except']['msg']
    assert r.json()['status'] == path_data['except']['status']
    assert r.json()['code'] == path_data['except']['code']
    #  2.检查实际有没有被注册(1.数据库;2.获取用户列表;3.用注册的用户登录)
    r = Member.getList(url, baserequests)
    print(r.text)
    assert phone in r.text


# 验证登录成功
def test_login_pass(path_data1, url, baserequests):
    print(f"测试数据为:{path_data1['casedata']}")
    print(f"预期结果为:{path_data1['except']}")
    r = Member.login(url, baserequests, path_data1['casedata'])
    #  1.检查响应结果
    assert r.json()['msg'] == path_data1['except']['msg']
    assert r.json()['status'] == path_data1['except']['status']
    assert r.json()['code'] == path_data1['except']['code']


# 验证登录失败
def test_login_fail(path_data2, db, url, baserequests):
    print(f"测试数据为:{path_data2['casedata']}")
    print(f"预期结果为:{path_data2['except']}")
    r = Member.login(url, baserequests, path_data2['casedata'])
    #  1.检查响应结果
    assert r.json()['msg'] == path_data2['except']['msg']
    assert r.json()['status'] == path_data2['except']['status']
    assert r.json()['code'] == path_data2['except']['code']

# 登录失败
# @pytest.fixture(params=DataRead.readyaml("ZongHe/data_case/login_fail.yaml"))
# def fail_data(request):  # 固定写法
#     return request.param
