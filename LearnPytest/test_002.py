'''
测试前置和后置
类和方法级别
1.测试前置、后置名字不能写错，pytest是通过名字来识别测试前置和后置的
2.不够灵活，比如test_001期望执行前置。但是test_002不期望执行前置，只能分开成两个文件去实现
'''


class Test002:  # pytest的命名规范，类是以Test开头的

    def setup_class(self):
        print("测试前置：类的方法执行前调用")

    def teardown_class(self):
        print("测试后置：类的放法执行后调用")

    def setup_method(self):  # 使用setup一样的效果
        print("每个方法前执行")

    def teardown_method(self):  # 使用teardown一样的效果
        print("每个方法后执行")

    def test_001(self):
        print("用例1")

    def test_002(self):
        print("用例2")
