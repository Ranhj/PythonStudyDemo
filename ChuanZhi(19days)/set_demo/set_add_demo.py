# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/8 10:24
# IDE:        PyCharm
# className:  set_add_demo.py

# 集合是可变类型，只能添加单一数据，如果添加数据序列会报错
# add()
s1 = {10, 20, 30}
s1.add(40)
print(s1)
# 集合有自动去重功能，如果增加的数据是集合已有的，则什么都不做，也不会报错
s1.add(40)
print(s1)
s1.add([1, 2, 3])
print(s1)   # 往集合里用add()直接添加数据序列会报错 TypeError: unhashable type: 'list'