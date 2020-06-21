"""
timedelta 对象表示两个 date 或者 time 的时间间隔, 可选参数为：days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0
timedelta实例之间支持数学运算
"""
from datetime import timedelta


# 创建一个timedelta实例a_day
a_day = timedelta(days=1)
# total_seconds方法：即时间间隔包含了多少秒。等价于 td / timedelta(seconds=1)
a_day.total_seconds()
a_day / timedelta(seconds=3600)


"""
date 对象代表一个理想化历法中的日期（年、月和日）, 必选参数为：year、month、day,参数要求如下：
MINYEAR <= year <= MAXYEAR、 1 <= month <= 12、 1 <= 日期 <= 给定年月对应的天数
"""
# date对象之间支持加减运算，运算结果为timedelta对象
from datetime import date
from datetime import timedelta


# date的today属性获取当前日期
date.today()
# 创建一个日期实例
a_date = date(year=2020, month=5, day=20)
# date对象的加减运算
b_date = a_date + timedelta(days=2)
# replace方法：返回一个具有同样值的日期，替换给出的某些形参的新值
a_date.replace(year=2000)
# timetuple方法：返回日期的tm_year, tm_mon, tm_mday, tm_hou, tm_min, tm_sec, tm_wday, tm_yday信息，其中时分秒信息自动补0，tm_wday表示日期是星期几，tm_yday表示日期是该年的第几天
a_date.timetuple()
# weekday方法：返回日期是星期几(从0开始，返回值0-6，例如周三返回值为2)
a_date.weekday()
# isoweekday方法：返回日期是星期几(从1开始，返回值1-7，例如周三返回值为3)
a_date.isoweekday()
# isoformat方法： 返回一个2020-05-20格式的日期
a_date.isoformat()
# ctime方法：返回一个代表日期的字符串,格式如Wed May 20 00:00:00 2020
a_date.ctime()
# strftime方法：按照参数指定的格式返回日期，例如"%d/%m/%Y"返回20/05/2020
a_date.strftime("%d/%m/%Y")


"""
time 对象代表一个时间对象, 可选参数hour=0, minute=0, second=0, microsecond=0，所有参数有范围限定
"""
from datetime import time


# 创建一个time实例
a_time = time(hour=12, minute=24)
# time的replace方法
# time的isoformat方法,参数timespec决定输出time效果
a_time.isoformat(timespec='seconds')
# time的strftime方法,按照参数指定的格式返回日期，例如"%H:%M:%S"返回12:24:00
a_time.strftime("%H:%M:%S")
# 也支持加减运算


"""
datetime 对象代表一个理想化历法中的日期和时间对象, 必选参数year, month, day，可选参数hour=0, minute=0, second=0, microsecond=0，所有参数有范围限定
"""
from datetime import datetime


# datetime的today属性获取当前日期、时间、微秒
a_datetime = datetime.today()
# datetime的now属性获取当前日期、时间、微秒(不指定时区时与today属性一样)
# datetime的date方法,获取date相关属性
a_datetime.date()
# datetime的time方法，获取time相关属性
a_datetime.time()
# 其他方法参考date对象(也支持加减运算)