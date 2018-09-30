# psutil是获取系统信息的第三方模块

import psutil

count = psutil.cpu_count()
print(count)
times = psutil.cpu_times()
print(times)

# for i in range(10):
#     print(psutil.cpu_percent(interval=1, percpu=True))

# 获取内存信息
print(psutil.virtual_memory())  # 物理内存
print(psutil.swap_memory())  # 交换内存

# 获取磁盘信息
counters = psutil.net_io_counters()
print(counters)

# 获取网络信息
addrs = psutil.net_if_addrs()
print(addrs)

# 获取网络状态
stats = psutil.net_if_stats()
print(stats)

# 获取进程信息
pids = psutil.pids()
print(pids)
process_iter = psutil.process_iter(20183)  # 指定进程ID
print(process_iter)
