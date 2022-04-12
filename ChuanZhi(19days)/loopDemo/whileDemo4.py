# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author: Rhj
# Datetime: 2022/3/2 15:50
j = 0
while j < 5:
    i = 0
    while i < 5:
        print('*',end=' ')
        i += 1
    j += 1
    print()

j = 0
while j <= 4:
    i = 0
    while i <= j:
        print('*', end=' ')
        i += 1
    print()
    j += 1
