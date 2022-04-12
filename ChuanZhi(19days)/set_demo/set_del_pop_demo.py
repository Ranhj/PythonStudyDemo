# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/8 10:40
# IDE:        PyCharm
# className:  set_del_pop_demo.py

# pop() 随机删除某个数据，并返回这个数据
s1 = {10, 20, 30}
del_num = s1.pop()
print(del_num)      # 10
print(s1)           # {20, 30}
del_num2 = s1.pop()
print(s1)           # {30}
del_num2 = s1.pop() # 随机删除可以直到全部删除完，删完后打印：set()
print(s1)