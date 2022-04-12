# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/22 17:28
# IDE:        PyCharm
# Title:      module_from_import_as_demo.py
# as 定义别名
"""
import 模块名 as 别名
from 模块名 import 功能名 as 别名
"""
# 模块别名
import time as tt
tt.sleep(1)
# time.sleep(2)   # 定义了别名后就不能再用原来的time去调用功能了，否则会报错：NameError: name 'time' is not defined
print('Hello')

# 功能别名
from time import sleep as sl
sl(2)
print('Hi')