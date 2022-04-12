# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/15 16:32
# IDE:        PyCharm
# Title:      func_lambda_listdatakeysort_demo.py
# 列表数据按字典key的值排序，用reverse=True 来做降序
# sort(key=lambda..., reverse=bool数据)
students = [{'name': 'Jack', 'age': 18},
            {'name': 'Tom', 'age': 20},
            {'name': 'Lily', 'age': 17},
            {'name': 'Miss Chen', 'age': 22}
            ]
# 按name值升序排列
# students.sort(key=lambda x: x['name'])  # [{'name': 'Jack', 'age': 18}, {'name': 'Lily', 'age': 17}, {'name': 'Miss Chen', 'age': 22}, {'name': 'Tom', 'age': 20}]
# 按name值降序排列
# students.sort(key=lambda x: x['name'], reverse=True)    # [{'name': 'Tom', 'age': 20}, {'name': 'Miss Chen', 'age': 22}, {'name': 'Lily', 'age': 17}, {'name': 'Jack', 'age': 18}]
# 按age值升序排列
# students.sort(key=lambda x: x['age'])   # [{'name': 'Lily', 'age': 17}, {'name': 'Jack', 'age': 18}, {'name': 'Tom', 'age': 20}, {'name': 'Miss Chen', 'age': 22}]
# 按age值降序排列
students.sort(key=lambda x: x['age'], reverse=True) # [{'name': 'Miss Chen', 'age': 22}, {'name': 'Tom', 'age': 20}, {'name': 'Jack', 'age': 18}, {'name': 'Lily', 'age': 17}]
print(students)