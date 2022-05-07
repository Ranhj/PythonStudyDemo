# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-05-05 15:50
# className:  set_demo.py
# s = [1, 2, 3, 3]
# s1 = set(s)
# print(s1, type(s1))

# 列表、字典  不可哈希，
# l = [[1, 2], 'hello', 'hi']
# s2 = set(l)
# print(s2, type(s2)) # TypeError: unhashable type: 'list'
#
# ll = [{'a': "b"}, 'hello', 'hi']
# s3 = set(l)
# print(s3, type(s3)) # TypeError: unhashable type: 'list'


# a = hash(('abc', '一二三'))
# print(a)    # 可哈希  -8448370811309014555
#
# b = hash(['hello', '123'])
# print(b)    # 不可哈希  TypeError: unhashable type: 'list'

# li = [1, 'a', 'b']
# s = set(li)
# # dic = {s: '123'}    # TypeError: unhashable type: 'set'
# # s.update([12, 'abc']) # 添加
# # s.remove('a')   # 指定删除
# # s.pop()   # 随机删除
# # s.clear() # 清空
# # del s   # 错误： NameError: name 's' is not defined
# print(s)

# print(set('abc') == set('abc'))  # True
# print(set('abc') < set('abcd'))  # True
# print(set('abcd') < set('abce'))    # False
# print(set('abc') and set('abcd'))    # {'a', 'c', 'b', 'd'}
# print(set('abef') or set('abcd'))    # {'f', 'e', 'b', 'a'}

"""交集、并集、差集"""
a = set([1, 2, 3, 4, 5])
b = set([4, 5, 6, 7, 8])


# intersection()    交集interc
print(a.intersection(b))    # 等同于a&b  {4, 5}
print(a & b)    # {4, 5}


# union 并集
print(a.union(b))   # 等同于a|b  {1, 2, 3, 4, 5, 6, 7, 8}
print(a | b)    # {1, 2, 3, 4, 5, 6, 7, 8}


# difference 差集
print(a.difference(b))  # {1, 2, 3}  等同于a-b  --in a but not in b
print(a-b)  # {1, 2, 3}

print(b.difference(a))  # {8, 6, 7}  等同于b-a  --in b but not in a
print(b-a)  # {8, 6, 7}


# symmetric_difference  对称差集
print(a.symmetric_difference(b))    # 等同于a^b  {1, 2, 3, 6, 7, 8}
print(a ^ b)    # {1, 2, 3, 6, 7, 8}


# 父集、超集
print(a.issuperset(b))  # 等同于a>b a是否完全包含b：False
print(a > b)    # False
print(a.issubset(b))    # 等同于a<b a是否是b的子集：False
print(a < b)    # False