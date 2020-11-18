import unittest
from LearnRequests.GetExcel import GetExcel
from parameterized import parameterized


class LoginTest(unittest.TestCase):

    @parameterized.expand(GetExcel().load(r'./CeShiTest.xlsx', 'zhuce'))
    def test_login_success(self, username, password):
        '''登陆成功功能测试用例'''
        try:
            self.page.login(username, password)
            # 断言
            real_name = self.page.get_login_name()

            # assert element.text=='admin'
            self.assertEqual(real_name, username, '登陆失败！')

            self.page.logout()

        except:
            raise NameError('测试失败！')

    @parameterized.expand(GetExcel().load(r'./data/data.xlsx', 'login_fail'))
    def test_login_fail(self, username, password):
        '''登陆失败工程测试用例'''
        try:
            self.page.login(username, password)
            self.logger.info('登陆完毕！')
            # 断言
            tip = self.page.get_fail_tips()
            self.assertEqual(tip, '登录失败，请检查您的成员名或密码是否填写正确。', '断言失败！')
            self.logger.info('断言成功！')
        except:
            self.logger.error('代码出错了，请赶紧排查')
            raise NameError('测试失败！')
        finally:
            self.page.confirm()
            self.logger.info('点击确定成功')


if __name__ == "__main__":
    unittest.main()
