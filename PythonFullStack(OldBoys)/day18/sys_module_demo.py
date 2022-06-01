# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-06-01 13:47
# className:  sys_module_demo.py
# python 解释器进行交互
"""
sys模块
"""
import sys

# 命令行参数List，第一个元素是程序本身路径
# print(sys.argv)
#
# def post():
#     print('ok')
#
# def download():
#     pass
#
# if sys.argv[1] == 'post':
#     post()
# elif sys.argv[1] == 'download':
#     download()


# 退出程序，正常退出时exit(0)
# sys.exit()


# 获取Python解释程序的版本信息
# print(sys.version)  # 3.8.0 (tags/v3.8.0:fa919fd, Oct 14 2019, 19:37:50) [MSC v.1916 64 bit (AMD64)]


# 最大的Int值   sys.maxint


# 返回模块的搜索路径，初始化时时使用PYTHONPATH环境变量的值
# print(sys.path)  # ['D:\\Study\\python_workspace\\PythonStudyDemo\\PythonFullStack(OldBoys)\\day18', 'D:\\Study\\python_workspace\\PythonStudyDemo', 'C:\\Users\\Sniper\\AppData\\Local\\Programs\\Python\\Python38\\python38.zip', 'C:\\Users\\Sniper\\AppData\\Local\\Programs\\Python\\Python38\\DLLs', 'C:\\Users\\Sniper\\AppData\\Local\\Programs\\Python\\Python38\\lib', 'C:\\Users\\Sniper\\AppData\\Local\\Programs\\Python\\Python38', 'C:\\Users\\Sniper\\AppData\\Local\\Programs\\Python\\Python38\\lib\\site-packages']


# 返回操作系统平台的名称
# print(sys.platform)  # win32

# import os
# if sys.platform == 'win32':
#     os.system('dir')
# else:
#     os.system('Ls')


# 标准输出
# sys.stdout.write('please')


# val = sys.stdin.readline()[:-1]

