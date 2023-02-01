# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-12-22 15:59
# className:  lianxi10.py
li = []
for i in range(1000):
    li.append(i)

while True:
    p = input('请输入要查看的页面：')
    p = int(p)
    start = (p-1) * 10
    end = p * 10
    print(li[start:end])