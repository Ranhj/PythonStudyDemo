# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/4 17:35
# IDE:        PyCharm
# className:  list_judge_in_demo2.py

username_list = ['Tom', 'Jack', 'Yang','浪子不浪']
username = input('请输入您要注册的用户名：')
if username in username_list:
    print(f'您输入的名字是"{username}", 该用户名已存在，请稍后重新输入！')
else:
    print(f'您输入的名字是"{username}", 可以注册该用户名~')