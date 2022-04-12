# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/22 11:33
# IDE:        PyCharm
# Title:      exceptionPassing_demo.py
# 异常的传递
# 需求：
#     1.尝试只读方式打开test01.txt文件，如果文件存在则读取文件内容，文件不存在则提示用户即可
#     2.读取内容要求：尝试循环读取内容，读取过程中如果检测到用户意外终止程序，则except捕获异常并提示用户
import time

try:
    f = open('test01.txt')
    # 尝试循环读取内容
    try:
        while True:
            con = f.readline()
            # 如果读取完成则退出循环
            if len(con) == 0:
                break
            time.sleep(1)
            print(con)
    except:
        # 在命令提示符中如果按下CTRL + C 结束终止的键
        print('程序意外终止')
    finally:
        f.close()
        print('文件已关闭')
except:
    print('该文件不存在')
