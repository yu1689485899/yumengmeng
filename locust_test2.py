'''
任务集合:分层的方式，按模块、子系统来管理
'''
from asyncio import Task

from locust import TaskSet, task, HttpUser, between


class SystemManage(TaskSet):
    @task
    def task1(self):
        self.client.get("/carRental/sys/toUserManager.action")

    @task
    def task2(self):
        self.client.get("/carRental/sys/toRoleManager.action")

    @task
    def task3(self):
        self.client.get("/carRental/sys/toLogInfoManager.action")


# 基础管理模块
class BasicManage(TaskSet):
    @task(7)
    def task1(self):
        self.client.get("/carRental/bus/toCustomerManager.action")

    @task(3)
    def task2(self):
        self.client.get("/carRental/bus/toCarManager.action")


class CarRentalTest(HttpUser):
    wait_time = between(1, 3)  # 任务之间的间隔时间
    # tasks = [BasicManage, SystemManage]  # 任务集合,task是uesr中定义的属性，不能写错
    tasks = {BasicManage: 4, SystemManage: 1}

    # 任务集合，后面数字表示权重，比如访问基础管理模块的人会比访问系统配置的人多3倍

    def on_start(self):  # 测试前置,登录，在开始运行时每个用户调用一次
        user = {"loginname": "admin", "pwd": "123456"}
        self.client.post("/carRental/login/login.action", data=user)

    def on_stop(self):  # 测试后置，退出登录，在结束运行时每个用户调用一次

        self.client.post("/carRental/logout/logout.action")  # 乱写的接口，执行时时失败的。

    # 达到类似serveragent的效果，在性能测试期间，获取cpu、内存的趋势
    # 死循环，每隔3s读一次，把读的结果写到文件中，测试结束后分析文件，使用excel生成图表
    # 时间戳 cpu% 内存% 磁盘% 发送字节数 接受字节数
