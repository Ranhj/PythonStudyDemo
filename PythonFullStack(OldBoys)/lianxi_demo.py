# !/usr/bin/env python
# _*_ coding: utf-8 _*_
# Author:     Ran_hj
# className:  lianxi_demo.py

"""学习中知识点练习集锦"""

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

"""dict增加键值对"""
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



"""dict追加操作"""
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



"""dict清空、删除操作"""
# # dict.clear() 清空
# dict7 = {'name': 'Tom', 'age': 20}
# dict7.clear()
# print(dict7)    # {}

# # del dict['key'] 删除指定键值对
# dict8 = {'name': 'Tom', 'age': 20}
# del dict8['name']
# print(dict8)    # {'age': 20}

# # dict.pop('key') 删除指定键值对，并返回该键值对的值
# dict9 = {'name': 'Tom', 'age': 20}
# dict9.pop('age')
# print(dict9)    # {'name': 'Tom'}

# # dict.popitem() 不指定就随机删除某组键值对，并以元组方式返回值
# dict10 = {'name': 'Tom', 'age': 20, 'hobby': 'guitar'}
# dict11 = dict10.popitem()
# print('随机删除的是：%s， 剩下的是：%s' % (dict11, dict10))
# # 随机删除的是：('hobby', 'guitar')， 剩下的是：{'name': 'Tom', 'age': 20}

# # del dict 删除整个字典
# dict12 = {'name': 'Tom', 'age': 20, 'hobby': 'guitar'}
# del dict12
# print(dict12)   # 都已经删除了，当然会报错： NameError: name 'dict12' is not defined

# # dict其他操作
# # 相当于给每一个key赋初始值
# dict13 = dict.fromkeys(['host1', 'host2', 'host3'], 'test')
# print(dict13)   # {'host1': 'test', 'host2': 'test', 'host3': 'test'}
# # 再指定某个key进行value值修改
# dict13['host3'] = 'aaa'
# print(dict13)

# dict14 = dict.fromkeys(['host1', 'host2', 'host3'], ['test', 'test2'])
# print(dict14) # {'host1': ['test', 'test2'], 'host2': ['test', 'test2'], 'host3': ['test', 'test2']}
# dict14['host2'][1] = 'test3'
# print(dict14) # {'host1': ['test', 'test3'], 'host2': ['test', 'test3'], 'host3': ['test', 'test3']}


'''dict 排序'''
# # sorted(dict) , sorted(dict.items()) 排序都是默认按照key来排序
# dict1 = {5:'555', 2:'222', 3:'333'}
# print(sorted(dict1))    # [2, 3, 5]
#
# dict2 = {5:'555', 2:'666', 3:'333'}
# print(sorted(dict2.items()))    # [(2, '666'), (3, '333'), (5, '555')]
#
# dict3 = {'name': 'Tom', 'age': 20, 'hobby': 'guitar'}
# print(sorted(dict3.items()))    # [('age', 20), ('hobby', 'guitar'), ('name', 'Tom')]


"""dict 循环遍历"""
# dict4 = {'name': 'Tom', 'age': 20, 'hobby': 'guitar'}
'''两种运行结果均为：
name Tom
age 20
hobby guitar
'''
# for i in dict4:             # 推荐这种方法
#     print(i, dict4[i])
#
# for i, v in dict4.items():  # 数据量大则不推荐，因为要转换，比较耗时
#     print(i, v)




"""
    String操作 练习demo
"""
# # 1.重复输出字符串
# print('W'*5)    # WWWWW
#
# # 2.过索引获取字符串中字符，和列表切片操作相同
# print('helloworld'[2:]) # lloworld
#
# # 3.关键字 in
# print('h' in 'hello')   # True
#
# # 4.格式字符串
# print('%s是一位好%s' % ('小明', '同志'))    # 小明是一位好同志
#
# # 5 字符串拼接 + ,   ''.join([,,])  注：+效率低，建议用join
# a = '123'
# b = 'abc'
# d = '一二三'
# c = a + b + d
# print(c)    # 123abc一二三
#
# c1 = ''.join([a, b, d])
# print(c1)   # 123abc一二三

#
"""String内置方法"""
# st = 'hello kitty'
#
# # 统计元素个数    .count('字符串')
# print(st.count('t'))    # 2
#
# # 字符串首字母转换为大写   .capitalize()
# print(st.capitalize())  # Hello kitty
#
#
#
# # 居中展示，两边指定字符填充 .center(要填充的数量, '用什么填充')
# print(st.center(50, '-'))   # -------------------hello kitty--------------------
# print('Hello'.center(50, '-'))  # ----------------------Hello-----------------------
# # 居左，右边用指定字符进行填充  .ljust(要填充的数量, '用什么填充')
# print('Hello'.ljust(50, '-'))   # Hello---------------------------------------------
# # 居右，左边用指定字符进行填充  .rjust(要填充的数量, '用什么填充')
# print('Hello'.rjust(50, '-'))   # ---------------------------------------------Hello
#
#
#
# # 判断是否以某个内容结尾，返回True/False    .endswith('字符串')
# print(st.endswith('ty'))    # True
#
# # 判断是否以某个内容开头，返回True/False  .startswith('字符串')
# print(st.startswith('H'))   # False
#
# #
# st1 = 'he\tllo python'
# print(st1.expandtabs(tabsize=10))   # he        llo python
#
# # 查找到第一个元素，并将索引值返回
# print(st.find('e')) # 1
#
# # 格式化输出的另一种方式
# st2 = 'hello kitty {name} is {age}'
# print(st2.format(name='Tom', age=20))               # hello kitty Tom is 20
# print(st2.format_map({'name': 'Jack', 'age': 18}))  # hello kitty Jack is 18
#
# # 返回指定子串的下标
# st3 = 'hello kitty'
# print(st3.index('i'))    # 7

# # 判断指定字符串至少有一个字符且所有字符都是字母或数字则返回 True， 否则返回 False
# print('abc'.isalnum())  # True
# print('123'.isalnum())  # True
# print('a1'.isalnum())   # True
# print('棉花'.isalnum())  # True
# print('**'.isalnum())   # False
# print(' '.isalnum())    # False
# print('a 1'.isalnum())  # False

#
# # 判断是否是十进制数
# print('a'.isdecimal())  # False
# print('10'.isdecimal()) # True
#
# # 判断返回的是否整型
# print('1'.isdigit())    # True
# print('1.2'.isdigit())  # False
# print('a'.isdigit())    # False
#
# # 判断变量名是否满足规则
# print('a'.isidentifier())   # True
# print('_a'.isidentifier())  # True
# print('*a'.isidentifier())  # False
# print('0a'.isidentifier())  # False
#
# # 判断是否全小写
# print('abc'.islower())  # True
# print('aBc'.islower())  # False
# print('ABC'.islower())  # False
#
# # 判断是否全大写
# print('ABC'.isupper())  # True
# print('aBC'.isupper())  # False
# print('abc'.isupper())  # False
#
# # 判断是否是空格
# print(' '.isspace())  # True
# print('1'.isspace())  # False
# print('1 '.isspace()) # False
#
# # 判断是否是title，title的要求是每个单词首字母大写
# print('My Title'.istitle())  # True
# print('My title'.istitle())  # False
# print('MY TITLE'.istitle())  # False
#
# # 将所有大写字母转换为小写字母
# print('MY TITLE'.lower())   # my title
# print('My Title'.lower())   # my title
# # 将所有小写字母转换为大写字母
# print('my title'.upper())   # MY TITLE
# print('My Title'.upper())   # MY TITLE
# # 将原有的大小写字母全部反转：大变小、小变大
# print('Ab'.swapcase())  # aB
# print('AB'.swapcase())  # ab
# print('ab'.swapcase())  # AB
#
# # 去掉字符串中的空格等，包括前、后的
# print('    My Title'.strip())
# print('My Title    '.strip())
#
# # 替换字符串 .replace('旧字符串', '新字符串', '替换次数')
# print('My Title'.replace('My', 'You'))  # You Title
# print('My My Title'.replace('My', 'You'))  # You You Title
# print('My My Title'.replace('My', 'You', 1))  # You My Title  # 添加一个参数 1， 表示只替换一次
#
# # 返回目标子串处于字符串中从右往左第一次出现的下标
# print('My two Title'.rfind('t'))    # 9
#
# # 指定用什么来分割字符串，并返回一个列表
# print('My Title'.split(' '))    # ['My', 'Title']
# print('hello'.split('e'))       # ['h', 'llo']  # e被用来作为分隔符了
#
# # 从右边开始查找并指定用什么来分割，添加参数指定分割次数
# print('My two Title'.rsplit('t', 1))    # ['My two Ti', 'le']
# print('My two Title ata'.rsplit('t', 1))    # ['My two Title a', 'a']
# print('My two Title ata'.rsplit('t', 2))    # ['My two Ti', 'le a', 'a']
#
# # 将指定字符串转换为title，title的要求是每个单词首字母大写
# print('my title'.title())   # My Title

# python代码可以写一行，用分号隔开
# a = 'Hello'; b = 'How are you?'; print(a); print(b); print(a+b)

# python2运行
# s = "特斯拉"
# s_to_unicode = s.decode("utf-8")
# unicode_to_gbk = s_to_unicode.encode("gbk")
# print(s)
# print(s_to_unicode)
# print(unicode_to_gbk)


# import sys
# print(sys.getdefaultencoding()) # 查看默认编码


"""day 8"""
# 能调用方法的一定是对象


# import sys, time
#
# for i in range(30):
#     sys.stdout.write('*')
#     sys.stdout.flush()
#     time.sleep(0.1)
#
# for i in range(30):
#     print('*', end='', flush=True)
#     time.sleep(0.1)
#
# a = str({'北京':{'1': '111'}})
# print(type(a))  # <class 'str'>
# a = eval(a) # 将字符串格式转换为字典格式
# print(type(a))  # <class 'dict'>
# print(a['北京'])  # {'1': '111'}

# import time
# for i in range(1,10):
#     time.sleep(1)
#     print(i)

# b = r"he is happy \n Yes"
# b2 = repr("he is happy \n Yes")
# b3 = str("he is happy \n Yes")
# print(b)
# print(b2)
# print(b3)

# print(dir(str))
# # ['__add__', '__class__', '__contains__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__getnewargs__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mod__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__rmod__', '__rmul__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'capitalize', 'casefold', 'center', 'count', 'encode', 'endswith', 'expandtabs', 'find', 'format', 'format_map', 'index', 'isalnum', 'isalpha', 'isascii', 'isdecimal', 'isdigit', 'isidentifier', 'islower', 'isnumeric', 'isprintable', 'isspace', 'istitle', 'isupper', 'join', 'ljust', 'lower', 'lstrip', 'maketrans', 'partition', 'replace', 'rfind', 'rindex', 'rjust', 'rpartition', 'rsplit', 'rstrip', 'split', 'splitlines', 'startswith', 'strip', 'swapcase', 'title', 'translate', 'upper', 'zfill']

# a = 1
# b = 2
# a = b
#
# print(a)
# print(b)
#
# a1 = 3
# b1 = a1
# b1 = 4
#
# print(a1)
# print(b1)

# i = [[1, 2], 3, 4]
# j = i
# # j[1] = 33
# j[0] = 11, 22
# k = j.copy()
# k[2] = 444444
# i.clear()
# print(f'i:{i}') # i:[]
# print(f'j:{j}') # j:[]
# print(f'k:{k}') # k:[(11, 22), 3, 444444]


# s1 = set('what')
# print(s1)
#
# s1.update('is')
# print(s1)
#
# s1.add('you')
# print(s1)

# s2 = set([1, 3])
# s3 = set([1, 2, 3, 4])
# print(s2)
# print(s3)
# print(s2 < s3)
# print(s2 > s3)
# print(s2 == s3)
# s4 = s2 & s3
# print(s4)


# def f(**kwargs):
#     print(kwargs)
#
# # f(info={'name': "Lily"})    # {'info': {'name': 'Lily'}}
# f(**{'name': "Lily"})   # {'name': 'Lily'}  要想直接传入字典，可以在前面加上**


# a = [x for x in range(10)]
# print(a)    # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# t = ('aaa', 6, 9)
# a, b, c = t
# # a = t[0]
# # b = t[1]
# print(a)    # aaa
# print(b)    # 6


# import time
# start_time = time.time()
# list = [x for x in range(100000000)]
# print(list)
# end_time = time.time()
# print('spend: %s' % (end_time - start_time))

from collections import Iterator
# print(isinstance([1,2],list))   # True
# print(isinstance('a',list))     # False

# import re
# ret = re.search('\([^()]+\)', '(1+(2+5)*2)')
# print(ret.group())  # (2+5)

import os
# print(os.path.abspath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))
# print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
"""
D:\Study\python_workspace\PythonStudyDemo\PythonFullStack(OldBoys)\lianxi_demo.py
D:\Study\python_workspace\PythonStudyDemo\PythonFullStack(OldBoys)
D:/Study/python_workspace/PythonStudyDemo/PythonFullStack(OldBoys)/lianxi_demo.py:462: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated since Python 3.3, and in 3.9 it will stop working
"""

# """验证码"""
# import random
#
# def v_code():
#
#     code = ''
#     for i in range(4):
#
#         num = random.randint(0, 9)
#         alf = chr(random.randint(65, 90))
#         add = random.choice([num, alf])
#         code += str(add)
#     return code
#
# print(v_code())


# import json
# x = "[null,true,false,1]"
# print(eval(x))
# print(json.loads(x))

# 封装
class Bar:
    def __init__(self, n, a):
        self.name = n
        self.age = a
        self.gender = '男'

    def Person(self):
        print(self.name, self.age, self.gender)

p1 = Bar('Jack', 18)
p1.Person()