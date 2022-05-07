# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-05-05 10:34
# className:  copy_demo.py
# 深浅拷贝

# s = [1, "alex", 'alvin']
# s2 = s.copy()   # 将s copy给s2
# print(s2)   # [1, 'alex', 'alvin']
#
# s2[0] = 3   # 重新给s2第一个元素赋值
# print(s2)   # [3, 'alex', 'alvin'] 赋值成功
# print(s)    # [1, 'alex', 'alvin'] 对原始的s并无影响

# 浅拷贝，只会拷贝第一层，不会拷贝第二层，列表中的列表或者字典就属于第二层
# 修改复制后的字符元素不影响原数据，但是修改复制后的列表元素会同步修改原数据
# s3 = [[1, 2], "alex", 'alvin']
# s4 = s3.copy()
# # s4 = s3[:]  # 等同于s4 = s3.copy()
# print(s3)
# print(s4)
# s4[1] = 'Jack'
# print(s3)
# print(s4)
# s4[0][1] = 3
# print(s4)
# print(s3)
#
# # 模拟银行关联账户
# husband = ['zhangsan', 123, [10000, 5000]]
# wife = husband.copy()
# wife[0] = 'xiaohong'
# wife[1] = 345
# wife[2][1] -= 1500  # wife取了1500
# print(husband)  # ['zhangsan', 123, [10000, 3500]]
# husband[2][1] += 10000  # husband存了10000
# print(wife)     # ['xiaohong', 345, [10000, 13500]]

# 深拷贝
import copy
# 模拟银行关联账户
husband = ['zhangsan', 123, [10000, 5000]]
wife = husband.copy()
wife[0] = 'xiaohong'
wife[1] = 345

# xiaosan = copy.copy()   # 浅拷贝：shallow copy
xiaosan = copy.deepcopy(husband)   # 深拷贝：deepcooy
xiaosan[0] = 'xiaofang'
xiaosan[1] = 222
xiaosan[2][1] -= 3000
husband[2][1] -= 1000
print(wife)  # ['xiaohong', 345, [10000, 4000]]
print(xiaosan)  # ['xiaofang', 222, [10000, 2000]]
