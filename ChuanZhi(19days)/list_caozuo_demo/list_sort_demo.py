# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/5 11:08
# IDE:        PyCharm
# className:  list_sort_demo.py

# sort() 排序     reverse=False:升序排序  reverse=True:降序排序
list1 = [1, 3, 2, 8, 4, 6, 7, 9, 5]
list1.sort()                            # 默认不写就是按升序排序
list1.sort(key=None, reverse=False)     # reverse=False:升序排序(默认)   [1, 2, 3, 4, 5, 6, 7, 8, 9]
list1.sort(reverse=True)                # reverse=True:降序排序         [9, 8, 7, 6, 5, 4, 3, 2, 1]
print(list1)
