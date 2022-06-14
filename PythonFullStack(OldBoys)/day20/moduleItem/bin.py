# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-06-13 15:20
# className:  bin.py


# import calculate    # 通过搜索路径找到calculate.py后，将calculate.py把calculate.py模块里的所有代码都解释了一遍
#
# import sys
# #
# # print(calculate.add(1, 2))  # 3
# #
# # # 搜索路径： sys.path
# # print(sys.path) # ['D:\\Study\\python_workspace\\PythonStudyDemo\\PythonFullStack(OldBoys)\\day20\\module_item_demo', 'D:\\Study\\python_workspace\\PythonStudyDemo', 'C:\\Users\\Sniper\\AppData\\Local\\Programs\\Python\\Python38\\python38.zip', 'C:\\Users\\Sniper\\AppData\\Local\\Programs\\Python\\Python38\\DLLs', 'C:\\Users\\Sniper\\AppData\\Local\\Programs\\Python\\Python38\\lib', 'C:\\Users\\Sniper\\AppData\\Local\\Programs\\Python\\Python38', 'C:\\Users\\Sniper\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages']
# #
# # print(x)
# print(calculate.x)

# from calculate import add, sub  # 从模块调用方法
# print(add(1, 4))    # 5
# print(sub(10, 2))   # 8

# from calculate import * # 为防止自写模块和库模块冲突，所以建议不要用这种导入方式
# # print(add(1, 3))    # 4
# # print(x)    # 3.3333
#
# def add(x, y):
#     return x + y + 2
# print(add(1, 2))

# from calculate import add as plus
# # print(add(1, 2))    # NameError: name 'add' is not defined
# print(plus(1, 2))   # 3

# import web.logger
# logger.logger() # NameError: name 'logger' is not defined
# from web import logger
# logger.logger() # logging

# from web.web2 import logger
# logger.logger() # logging...
# from web.web2 import logger.logger
# logger()    # SyntaxError: invalid syntax

# from web.web2.logger import logger
# logger()    # logging...

# import web  # ok

from web import  main
print(main.x)   # 123
