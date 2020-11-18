from cmath import e

import null
import pytest
import requests


def register(data):
    url = "http://jy001:8081/futureloan/mvc/api/member/register"
    r = requests.post(url, data=data)
    return r


@pytest.fixture(params=[{"casedata": {"mobilephone": "137123456789", "pwd": "123456abc", "regname": "aaa"},
                         "except": {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}, },
                        {"casedata": {"mobilephone": "137", "pwd": "123456abc", "regname": "aaa"},
                         "except": {"status": 0, "code": "20109", "data": None, "msg": "手机号不能为空"}, },
                        {"casedata": {"mobilephone": "1371234111a", "pwd": "123456abc", "regname": "aaa"},
                         "except": {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}, },
                        {"casedata": {"mobilephone": "null", "pwd": "123456abc", "regname": "aaa"},
                         "except": {"status": 0, "code": "20109", "data": None, "msg": "手机号码格式不正确"}, },
                        {"casedata": {"mobilephone": "", "pwd": "123456", "regname": "aaa"},
                         "except": {"status": 0, "code": "20103", "data": None, "msg": "手机号不能为空"}, }
                        ])
def data1(request):
    return request.param


def test_login4(data1):
    # # 测试步骤
    real = register(data1["casedata"])
    assert real.json()['msg'] == data1['except']['msg']
    print(f"使用手机号{data1['casedata']['mobilephone']}注册显示{data1['except']['msg']}")
