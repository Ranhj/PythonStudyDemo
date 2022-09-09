# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-09-09 16:55
# className:  lianxi07.py
class Province:
    # 静态字段，属于类
    country = '中国'

    def __init__(self, name):
        # 普通字段，属于对象
        self.name = name

henan = Province("河南")
hebei = Province("河北")
print(Province.country)
