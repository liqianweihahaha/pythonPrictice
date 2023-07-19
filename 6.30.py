"""
python常用模块之时间模块 time() 和 datatime（）

"""
# import time
#
#
# time_stamp = time.time()
# print(time_stamp)  # 输出当前时间戳
#
# time_localtime = time.localtime()
# print(time_localtime)  # 输出当前时间元组
#
# struct_time = time.gmtime(time_stamp)
# print(struct_time)   # gmtime（）将时间戳 转换成 时间元组
#
# time_stamp1 = time.mktime(struct_time)  # mktime（） 将时间元组转换成时间戳
# print(time_stamp1)
#
# time_striftime = time.strftime("%Y/%m/%d",struct_time)  # 将时间元组  按一定的时间格式 输出
# print(time_striftime)
#
# time_striptime = time.strptime("2023/06/30","%Y/%m/%d")    # 将格式化的时间 转换成 时间元组
# print(time_striptime)
#
#
# time_string_en = time.asctime(struct_time)  # 将时间元组 转换成 英文字符串时间
# print(time_string_en)  # Fri Jun 30 02:59:16 2023
#
# time_string_en1 = time.ctime(time_stamp)  # 将时间戳 转换成 英文字符串时间
# print(time_string_en1)  # Fri Jun 30 11:01:15 2023
#
#
#
# import datetime
#
# now_time = datetime.datetime.now()    # 1、datetime()获取当前时间
# print(now_time)  # 2023-06-30 11:05:30.714477
#
# now_date = datetime.datetime.now().date()  # 2、获取当前日期
# print(now_date)  # 2023-06-30
#
# time_strftime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")  # 将当前时间 进行格式转换
# print(time_strftime)  # 2023-06-30 11:12:42
#
#
# """
# python中计算两个日期之间的天数
# """
# date1 = datetime.datetime(2018,10,3)    # 2018-10-03 00:00:00
# date2 = datetime.datetime(2019,10,1)    # 2019-10-03 00:00:00
# s = date2 - date1   # 363 days, 0:00:00
# print(s.days)    # 363

# -----------------------------------------------------------------------------

"""
python常用模块之random（）
"""
import random

# 1、获取随机浮点数
print(random.random()) # 返回0-1之间的随机浮点数
print(random.uniform(1,100))  # 返回a--b 之间的随机实数

# 2、获取随机整数
print(random.randint(1,100))  # 返回a--b之间的随机整数
print(random.randrange(1,100,2))  # 返回1-100之间的随机奇数

# 3、获取随机字符
print(random.choice('rwerwrwerwer234234rwerwerwrwer'))  # 从序列中返回一个随机元素
print(random.sample('weruwiruw324234234',3))     #['w', '4', 'i']  从序列中返回n个随机元素


"""
随机模块的应用：实现四位验证码
"""

import random
import string

str_source = string.ascii_letters + string.digits
str_list = random.sample(str_source,7)

str_final = ''.join(str_list)
print(str_final)   # 验证码：0vlGrFt






