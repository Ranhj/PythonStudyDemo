# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author: Rhj
# Datetime: 2022/3/2 14:35
i = 1
while i <= 5:
    print(f'吃第{i}个苹果！')
    i += 1
    if i == 4:
        print(f'吃了{i-1}个了，吃饱了不吃啦~')
        break
