# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/3 17:16
# IDE:        PyCharm
# className:  stringCaoZuoDemo.py
mystr = 'What is your name ? My name is Rhj!'
# 1. find()
print(mystr.find('is'))             # 5
print(mystr.find('is', 1, 10))      # 5
print(mystr.find('is', 15, 30))     # -1 ，返回-1，说明在指定位置没有查找到该子串
print(mystr.find('are'))            # -1， 返回-1，说明在字符串中没有查找到该子串

# 2. index()
print(mystr.index('is'))            # 5
print(mystr.index('is', 1, 10))     # 5
# print(mystr.index('is', 15, 30))    # 报错：ValueError: substring not found。查找该子串不存在，会报错!
# print(mystr.index('are'))           # 报错：ValueError: substring not found。查找该子串不存在，会报错!

# 3. count()
print(mystr.count('is'))            # 2 查找到出现2次
print(mystr.count('is', 1, 10))     # 1 在指定范围查找到1次
print(mystr.count('are'))           # 0 没有查找到该字串，所以显示0

# 4. rfind()
print(mystr.rfind('is'))            # 28 从右边开始查找
print(mystr.rfind('are'))           # -1 该子串不存在，报-1

# 5. rindex()
print(mystr.rindex('is'))           # 28 从右边开始查找
# print(mystr.rindex('are'))        # 报错：ValueError: substring not found。查找该子串不存在，会报错!
