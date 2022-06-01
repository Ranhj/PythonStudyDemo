# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-05-23 16:17
# className:  timeModule_demo.py
# 时间戳，结构化时间，格式化时间

import time
# print(help(time))
# print(time.time())  # 1653293961.6847956 时间戳  打印当前时间（时间戳是自 1970 年 1 月 1 日（00:00:00 GMT）以来的秒数。它也被称为 Unix 时间戳（Unix Timestamp）。单位是秒，可以转换为毫秒）
# time.sleep(3)
# print(time.clock()) # 计算CPU执行时间
# print(time.gmtime())    # time.struct_time(tm_year=2022, tm_mon=5, tm_mday=23, tm_hour=8, tm_min=26, tm_sec=35, tm_wday=0, tm_yday=143, tm_isdst=0)
# print(help(time.strftime('')))

## 字符串时间
# struct_time = time.localtime()
# print(time.strftime('%Y--%m--%d %H:%M:%S', struct_time)) # 2022--05--23 16:41:18
#
## 转换为结构化时间
# print(time.strptime('2022-05-23 16:49:01', '%Y-%m-%d %H:%M:%S'))    # time.struct_time(tm_year=2022, tm_mon=5, tm_mday=23, tm_hour=16, tm_min=49, tm_sec=1, tm_wday=0, tm_yday=143, tm_isdst=-1)

## 可以单独取年月日等的值
# a = time.strptime('2022-05-23 16:49:01', '%Y-%m-%d %H:%M:%S')
# print(a.tm_year)    # 2022
# print(a.tm_mon)     # 5
# print(a.tm_mday)    # 23
# print(a.tm_wday)    # 0 0是周一


# print(time.ctime())     # Mon May 23 17:02:42 2022
# print(time.ctime(1653296531))   # Mon May 23 17:02:11 2022
# print(time.mktime(time.localtime()))    # 转换时间戳  1653297463.0


import datetime
print(datetime.datetime.now())  # 2022-05-23 17:19:37.132402
