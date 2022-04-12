# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/17 16:17
# IDE:        PyCharm
# Title:      file_folder_operation_demo.py
# 文件和文件夹操作：重命名(文件、文件夹)  删除  新建文件夹   删除指定文件夹  获取当前所在目录   改变默认目录  获取某个文件夹下所有文件
"""
1.导入模块os
2.使用模块内功能
"""
import os
# 1.rename(原文件名， 新文件名):重命名文件
# os.rename('file6.txt', 'file66.txt')

# 1.1 rename(原文件夹名， 新文件夹名)：重命名文件夹
# os.rename('aaa', 'aaaa')
# os.rename('aaaa\\bbb', 'bbbb')  # 可以指定路径

# 2.remove(要删除的文件名):删除
# os.remove('file66.txt')     # 再次删除已删除的文件会报错

# 3.mkdir(路径：新文件名)：创建文件夹
# os.mkdir('D:\\desktop\\abc')    # 再次创建同名文件夹会报错

# 4.rmdir(路径：要删除的文件夹)：删除文件夹
# os.rmdir('D:\\desktop\\abc')  # 再次删除同名文件夹会报错

# 5.getcwd():获取当前目录 --必要要进入当前py文件里才能获取得到目录
# print(os.getcwd())  # D:\workpython\PycharmProjects\python\pythonStudy2022\pythonStudy(chuanzhirumen19days)\file_demo

# 6.chdir(目录)：改变默认目录
# 需求：在aaa文件夹里面创建bbb文件夹
# os.mkdir('aaa')     # 先创建aaa文件夹
# os.chdir('aaa')     # 改变默认目录为aaa目录 --如果不改目录就创建bbb目录，创建的bbb目录和aaa目录就是并列的同级目录了
# os.mkdir('bbb')     # 再创建的bbb文件夹就是存在于aaa文件夹里面了

# 7.listdir(目录)：获取某个文件夹下所有文件，返回一个列表
# print(os.listdir)       # <built-in function listdir>
# print(os.listdir())     # ['file_seek_demo.py', 'file_zhufangwenmoshi_demo.py', 'file_zhufangwenmoshi_demo2.py']
# print(os.listdir('aaa'))    # ['bbb'] 返回刚才创建的aaa目录里的bbb目录
# print(os.listdir('D:\\desktop\\abc'))   # 可以返回指定某路径下的文件夹
