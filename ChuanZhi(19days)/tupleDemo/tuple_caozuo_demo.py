# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/5 17:44
# IDE:        PyCharm
# className:  tuple_caozuo_demo.py
# tuple操作的函数
t1 = ('aaa', 'bbb', 'ccc','bbb')
# 1.通过下标查找
print(t1[0])            # aaa 返回下标0所在的数据
# 2.index()
print(t1.index('aaa'))  # 0  返回查找数据的下标
# print(t1.index('a'))    # ValueError: tuple.index(x): x not in tuple 查找不到报错
# 3.count()
print(t1.count('bbb'))  # 2  返回查找数据在元组中出现的次数
print(t1.count('b'))    # 0  没有查找到b，所以返回0次
# 4. len()
print(len(t1))          # 4  返回元组包含的数据个数
