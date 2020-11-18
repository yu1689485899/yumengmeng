"""
监控代码：监控服务器的内存、cpu、网络、磁盘等。与租车系统部署到一起
"""
from asyncio import sleep
from datetime import datetime

import psutil

print(psutil.cpu_percent())  # 获取cpu的信息
print(psutil.virtual_memory())  # 虚拟的内存
print(psutil.virtual_memory().percent)  # 虚拟内存的百分比
print(psutil.disk_usage("d:/"))  # 租车系统所在的磁盘
print(psutil.disk_usage("d:/").percent)  # 租车系统所在的磁盘百分比
print(psutil.net_io_counters())  # 网络
print(psutil.net_io_counters().bytes_sent)  # 发送的字节数
print(psutil.net_io_counters().bytes_recv)  # 接收的字节数
print(333)
# for i in range(3):
#     print(psutil.cpu_percent())  # 获取cpu的信息
#     print(psutil.virtual_memory())  # 虚拟的内存
#     print(psutil.virtual_memory().percent)  # 虚拟内存的百分比
#     print(psutil.disk_usage("d:/"))  # 租车系统所在的磁盘
#     print(psutil.disk_usage("d:/").percent)  # 租车系统所在的磁盘百分比
#     print(psutil.net_io_counters())  # 网络
#     print(psutil.net_io_counters().bytes_sent)  # 发送的字节数
#     print(psutil.net_io_counters().bytes_sent)  # 接收的字节数
with open("d:/资源占用情况.txt", mode='a', encoding='utf-8') as file:
    file.write("时间戳\tcpu%\t内存%\t磁盘\t发送字节数\t接收字节数\n")
    print()
    while True:
        print("监控中。。。。。")
        file.write(datetime.strftime(datetime.now(), "%Y-%m-%d %H:%M:%S") + '\t')
        file.write(str(psutil.cpu_percent()) + "%\t")
        file.write(str(psutil.virtual_memory().percent) + "%\t")
        file.write(str(psutil.disk_usage("d:/").percent) + "%\t")
        file.write(str(psutil.net_io_counters().bytes_sent) + "%\t")
        file.write(str(psutil.net_io_counters().bytes_recv) + "%\n")
        file.flush()
        sleep(3)
