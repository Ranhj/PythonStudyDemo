# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-12-23 15:00
# className:  s1.py
import s2
inp = input('请输入要查看的URL：')
if hasattr(s2, inp):
    func = getattr(s2, inp)
    result = func()
    print(result)

else:
    print('404')