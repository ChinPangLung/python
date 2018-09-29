from datetime import datetime,timedelta

# 获取当前时间
now = datetime.now()
print(now)
print(type(now))

# 构造一个时间
d = datetime(2018, 9, 29, 12, 20)
dt = datetime(2018, 9, 29)
print(d)
print(dt)

# datetime转timestamp
timestamp = d.timestamp()
print(timestamp)

# timestamp转datetime
fromtimestamp = datetime.fromtimestamp(timestamp)
print(fromtimestamp)

# str转datetime
strptime = datetime.strptime('2018-9-29 12:23:29', '%Y-%m-%d %H:%M:%S')
print(strptime)
print(type(strptime))

# datetime转str
strftime = now.strftime('%a, %b %d %H:%M')
print(strftime)

# datetime加减
datetime_now = datetime.now()
print(datetime_now)

print(datetime_now+timedelta(hours=10))
print(datetime_now-timedelta(days=1))
print(datetime_now+timedelta(days=1,hours=10))