'''
1.接口测试场景比较难模拟，需要大量的工作才可以完成
2.依赖第三方的接口，但是第三方的接口没有开发完成
测试环境不充分的情况下，怎么去做接口测试，使用mock来模拟
'''
from unittest import mock

import requests


# class Alipay:
#     def zhifu(self, data):
#         # 接口功能尚未开发完成
#         # 接口地址、get/post\入参、返回值已经定义好
#         # 接口参数 :{"OraderId": "23165565", "Amount": 128.5, "Type": "支付宝"}
#         # 接口返回值:"code": 200, "msg": "支付成功" 201支付失败 202支付超时
#         r = requests.post("http://zhifubao.com/pay", data=data).json()
#         return r
#
#
# class TestMock:
#     def test_alipay(self):
#         # 对要模拟的类创建一个对象
#         alipay = Alipay()
#         # 模拟zhifu的返回值为{"code": 200, "msg": "支付成功"}
#         alipay.zhifu = mock.Mock(return_value={"code": 200, "msg": "支付成功"})
#         # 调用zhifu接口
#         data = {"OraderId": "23165565", "Amount": 128.5, "Type": "支付宝"}
#         r = alipay.zhifu(data)
#         print(r)


class Alipay1:
    def quxian(self, data):
        # 接口功能尚未开发完成
        # 接口地址、get/post\入参、返回值已经定义好
        # 接口参数 :{"OraderId": "23165565", "Amount": 128.5, "Type": "支付宝"}
        # 接口返回值:"code": 200, "msg": "支付成功" 201支付失败 202支付超时
        r = requests.post("http://jy001:8081/futureloan/mvc/api/member/withdraw", data=data).json()
        return r

    def chongzhi(self, data1):
        # 接口功能尚未开发完成
        # 接口地址、get/post\入参、返回值已经定义好
        # 接口参数 :{"OraderId": "23165565", "Amount": 128.5, "Type": "支付宝"}
        # 接口返回值:"code": 200, "msg": "支付成功" 201支付失败 202支付超时
        r = requests.post("http://jy001:8081/futureloan/mvc/api/member/recharge", data=data1).json()
        return r


class TestMock1:
    def test_alipay(self):
        # 对要模拟的类创建一个对象
        alipay = Alipay1()
        # 模拟zhifu的返回值为{"code": 200, "msg": "支付成功"}
        alipay.quxian = mock.Mock(return_value={'status': 1, 'code': '10001', 'data': None, 'msg': '取现成功'})
        # 调用zhifu接口
        data1 = {"mobilephone": "13649175338", "amount": 30}
        data = {"mobilephone": "13649175338", "amount": 12.52}
        r1 = alipay.chongzhi(data1)
        print(r1)
        assert r1['msg'] == "充值成功"
        assert r1['status'] == 1
        assert r1['code'] == '10001'

        r = alipay.quxian(data)
        print(r)
        assert r['msg'] == "取现成功"
        assert r['status'] == 1
        assert r['code'] == '10001'
