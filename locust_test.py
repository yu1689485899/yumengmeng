'''
性能测试
'''
import math

from locust import HttpUser, between, task, LoadTestShape

'''
1.为要模拟的用户定义一个类，从HttpUser继承
'''


class CarRental(HttpUser):
    # between 是User类中定义的一个方法
    # wait_time 是User类中定义的一个属性，表示等待时间
    wait_time = between(3, 8)  # 任务跟任务之间的等待时间在3~8之间取随机数

    @task
    def loadAllRent(self):
        #
        self.client.get("/carRental/rent/loadAllRent.action?page=1&limit=10")

    @task
    def loadAllMenu(self):
        self.client.get("/carRental/menu/loadAllMenu.action?page=1&limit=10")


class DoubleWave(LoadTestShape):

    min_users = 20
    peak_one_users = 60
    peak_two_users = 40
    time_limit = 600

    def tick(self):
        run_time = round(self.get_run_time())

        if run_time < self.time_limit:
            user_count = (
                (self.peak_one_users - self.min_users)
                * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 5) ** 2)
                + (self.peak_two_users - self.min_users)
                * math.e ** -(((run_time / (self.time_limit / 10 * 2 / 3)) - 10) ** 2)
                + self.min_users
            )
            return (round(user_count), round(user_count))
        else:
            return None
