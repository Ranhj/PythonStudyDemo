# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/5 10:21
# IDE:        PyCharm
# className:  list_extend_demo.py

# extend() 追加数据是一个序列，把数据序列里面的数据拆开然后逐一追加到列表的结尾；如果是追加的字符串，也会拆开追加
name_list = ['Tom', 'Jack', 'Yang']
name_list.extend('Jane')             # ['Tom', 'Jack', 'Yang', 'J', 'a', 'n', 'e']
name_list.extend(['张三', '李四'])     # ['Tom', 'Jack', 'Yang', '张三', '李四']
print(name_list)