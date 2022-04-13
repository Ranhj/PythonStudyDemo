# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# className:  lianxi_demo.py

'''学习中知识点练习'''

# a = [1, 2, 3, 4]
# b = sorted(a)
# print(b)    # [1, 2, 3, 4]

# t1 = (1, 2, 3, 4)
# print(t1[1:3])


# # .isdigit() 判断字符串是否是数字
# str = '1'
# print("str = '1': ", str.isdigit())    # true 只有当字符串只包含数字的时候才是true，否则就为False
# str2 = 'a'
# print("str2 = 'a': ", str2.isdigit())   # False
# str3 = 'a1'
# print("str2 = 'a1': ", str3.isdigit())   # False


# # enumerate 枚举
# lst = [1, 2, 3, 4, 5, 6]
# for index, value in enumerate(lst, 1):
#     print('%s, %s'% (index, value))


# a, b, c = (11, 22, 'cc')
# print(a)
# print(b)
# print(c)
# a1, b1, c1 = [11, 22, 'cc']
# print(a1)
# print(b1)
# print(c1)


# # 直接for循环遍历 和 for循环枚举遍历，for循环遍历可以指定索引
# list1 = [('a', 1), ('b', 2)]
# # for i in list1:
# #     print(list1.index(i), i)
# for index, value in enumerate(list1, 1):
#     # print('%s, %s' % (index, value))    # 使用占位符
#     print(index, '>>>', value)
#
# print(len(list1))    # 打印出列表长度：2


# a = 10
# b = a
# a = 15
# print(a, b)     # 15 10

# # dict 字典
# dict1 = {'name':{'a':1,'b':2}, 'age': 2}
# print(dict1['name'])

# dict2 = {{'a':1,'b':2}:'aa', 'age': 2}
# print(dict2)

# dict3 = {1 :'aa', 'age': 2}
# print(dict3)

# dict4 = {1 :'aa', 'age': 2, 'age':3}
# print(dict4)

# a = [1, 2, 3]
# a = list()
# print(a)
# print(type(a))

# # dict也可以用列表去转换式的创建
# dict1 = dict([['a', 1],])
# print(dict1)    # {'a': 1}

# # dict增加键值对
# dict1 = {'name': 'Jack'}
# dict1['age'] = 20
# print(dict1)    # {'name': 'Jack', 'age': 20}
# # .setdefault() 键存在，不改动，返回字典中相应的键对应的值；键不存在，在字典中增加新的键值对，并返回相应的值
# ret = dict1.setdefault('hobby', 'guitar')
# print(ret)   # guitar
# print(dict1)    # {'name': 'Jack', 'age': 20, 'hobby': 'guitar'}

# # dict取key、value、items值
# dic1 = {'name': 'Tom', 'age': 18}
# print(list(dic1.keys()))    # ['name', 'age']
# print(list(dic1.values()))  # ['Tom', 18]
# print(list(dic1.items()))   # [('name', 'Tom'), ('age', 18)]

# list2 = [1, 2, 3]
# list2[0] = 4
# print(list2)    # [4, 2, 3]

# # dict追加
# dict1 = {'name': 'Jack', 'age': 20}
# dict2 = {'1': '11', '2': '22'}
# dict1.update(dict2)
# print(dict1)    # {'name': 'Jack', 'age': 20, '1': '11', '2': '22'}
# print(dict2)    # {'1': '11', '2': '22'}
#
# # dict如果追加的key与value与原数据相同，则不修改
# dict3 = {'name': 'Tom', 'age': 18}
# dict4 = {'name': 'Tom'}
# dict3.update(dict4)
# print(dict3)    # {'name': 'Tom', 'age': 18}
#
# # dict如果追加的key值一致，value值不一致，会修改value值
# dict5 = {'name': 'Sun', 'age': 22}
# dict6 = {'name1': 'HanMeimei'}
# dict5.update(dict6)
# print(dict5)    # {'name': 'HanMeimei', 'age': 22}

