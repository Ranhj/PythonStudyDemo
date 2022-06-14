# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-06-07 10:54
# className:  RegEx_module_demo.py

import re
"""
正则表达式
2元字符： .  ^  $  *  +  ?  { }  [ ]  |  ( ) \

结论：
* 等价于{0， 正无穷}
+ 等价于{1， +oo}
? 等价于{0， 1}

正则表达式的方法：
1. findall():   返回所有满足匹配条件的结果，将所有结果都返回到一个列表里
2. search():    返回匹配到的第一个对象(object)，对象可以调用group()返回结果
                函数会在字符串内查找模式匹配，直到找到第一一个匹配然后返回一个包含匹配信息的对象，
                该对象可以通过group()方法得到匹配的字符串，如果字符串没有匹配，则返回None.
3. match():     同search，不过仅在字符串开始处匹配，也返回匹配到的第一个对象(object)，对象可以调用group()返回结果
4. split():     
ret = re.split('[ab]', 'abcd')  先按'a'分割得到''和'bcd'，再对''和'bcd'分别按'b'分割
print(ret)  # ['', '', 'cd']
"""

# s = 'hello world'
# print(s.find('d'))   # 10  索引
# ret = s.replace('ll', 'xx')
# print(ret)  # hexxo world
# print(s.split('w')) # ['hello ', 'orld']

# string提供的方法是完全匹配
# 引入正则 模糊匹配



# ret = re.findall('alex', 'dakjfldkjalexaslf')
# print(ret2)     # ['alex']


# ret = re.findall('w\w{2}l', 'hello world')
# print(ret)      # ['worl']

# 元字符

#  通配符  . 只能代指任意一个字符
# ret = re.findall('w..l', 'hello world')
# print(ret)      # ['worl']

# ret = re.findall('w.l', 'hello w\norld')
# print(ret)      # []

# ret = re.findall('w..l', 'hello w\t ld')
# print(ret)      # ['w\t l']


# ^符
# ret = re.findall('^h...o', 'hello world')
# print(ret)      # ['hello']

# ret = re.findall('^h...o', 'hjasoflhello')
# print(ret)      # ['hjaso']  只从开头开始匹配


# $符
# ret = re.findall('a..x$', 'hdkfjkdsajfalexkdjklaf')
# print(ret)  # [] 从最后取，不匹配所以取不到

# ret = re.findall('a..x$', 'hdkfjkdsajfkdjklafalex')
# print(ret)  # ['alex'] 取到了


# *符：重复匹配[0,+oo]匹配0到无穷个
# ret = re.findall('a..exe', 'kdjaalexekdfk')
# print(ret)  # ['aalexe']

# ret = re.findall('a.exe', 'kdjaalexekdfk')
# print(ret)  # ['alexe']

# ret = re.findall('ba*', 'jfdksajkbaaaaaaaa')
# print(ret)  # ['baaaaaaaa']

# ret = re.findall('.*', 'dljsafkljbaaaaaaa')
# print(ret)  # ['dljsafkljbaaaaaaa', '']


# +符：[1, +oo] 匹配1到无穷个
# ret = re.findall('ab+', 'kdjakfbja')    # +只对前面的字符ab有效
# print(ret)  # []找不到所以为空

# ret = re.findall('ab+', 'kdjasklabdd')
# print(ret)  # ['ab']

# ret = re.findall('a+b', 'aaaabdjfakdf')
# print(ret)  # ['aaaab']


# ?符[0,1]  匹配0到1个
# ret = re.findall('a?b', 'aaaabdkfjdavbdkb')
# print(ret)  # ['ab', 'b', 'b']


# {}符
# ret = re.findall('a{5}b', 'ab')
# print(ret)  # []

# ret = re.findall('a{5}b', 'daaaaab')
# print(ret)  # ['aaaaab']

# ret = re.findall('a{1,4}b', 'aaaab')    # {1，}等价于{1， +oo}
# print(ret)  # ['aaaab']

# 字符集
# ret = re.findall('a[c,d]x', 'acx')
# print(ret)  # ['acx']

# ret = re.findall('a[c,d]x', 'adx')
# print(ret)  # ['adx']

# ret = re.findall('a[c,d]x', 'acdx')
# print(ret)  # []

# ret = re.findall('[a-z]', 'adf')
# print(ret)  # ['a', 'd', 'f']

# []字符集： 取消元字符的特殊功能
# ret = re.findall('[w,.]', 'awdx.')
# print(ret)      # ['w', '.']

# ret = re.findall(',', 'a,b')
# print(ret)  # [',']

# ret = re.findall('[1-9]', 'safdsfsda5daf')
# print(ret)  # ['5']

# ret = re.findall('[1-9,a-z,A-Z]', 'sfsAa5da')
# print(ret)  # ['5'] # ['s', 'f', 's', 'A', 'a', '5', 'd', 'a']

# ^符 放在[]里，是取反
# ret = re.findall('[^t]', 'abctdef')
# print(ret)  # ['a', 'b', 'c', 'd', 'e', 'f']

# ret = re.findall('[^4,7]', '12345678')
# print(ret)  # ['1', '2', '3', '5', '6', '8']

# ret = re.findall('[^ab]', 'cde"acb"fgh')
# print(ret)  # ['c', 'd', 'e', '"', 'c', '"', 'f', 'g', 'h']


# \符
# 反斜杠后边跟元字符去除特殊功能
# 反斜杠后边跟(部分)普通字符实现特殊功能
'''
\d  匹配任何十进制数： 相当于类 [0-9] 
\D  匹配任何非数字字符： 相当于类[^0-9]
\s  匹配任何空白字符： 相当于类[\t\n\r\f\v]
\S  匹配任何非空白字符： 相当于类[^ \t\n\r\f\v]
\w  匹配任何字母数字字符： 相当于类[a-zA-Z0-9_]
\W  匹配任何非字母数字字符： 相当于类[^a-zA-Z0-9]
\b  匹配一个特殊边界，也就是指单词和空格间的位置
'''
# print(re.findall('\d{11}', 'adaf12345678901dafd'))  # ['12345678901']
# print(re.findall('\d{11}', 'adaf123456789012345678901233dafd'))   # ['12345678901', '23456789012']
# print(re.findall('\sasd', 'fakasd'))    # []
# print(re.findall('\sasd', 'fak asd'))    # [' asd']
# print(re.findall('\wasd', 'fak asd'))    # []
# print(re.findall('\w', 'fak asd'))    # ['f', 'a', 'k', 'a', 's', 'd']
# print(re.findall(r'I\b', 'hello, I am a LIST'))  # ['I']
# print(re.findall(r'\bI', 'hello Iam a LIST'))  # ['I']

# 匹配出第一个满足条件的结果
# print(re.search('sb', 'skkddldsb')) # <re.Match object; span=(7, 9), match='sb'>
# ret = re.search('s.b', 'skkddldsab')
# print(ret.group())  # sab

# ret = re.search('a\.', 'a.gj').group()
# print(ret)  # a.

# ret = re.search('a\+', 'a+gj').group()
# print(ret)  # a+

# ret = re.findall(r'\\', 'adhf\d')
# print(ret)  # ['\\']


# ret = re.search('\bblow', 'blow')
# print(ret)  # None
# ret = re.search(r'\bblow', 'blow')
# print(ret)  # <re.Match object; span=(0, 4), match='blow'>

# 元组字符之分组()
# m = re.findall(r'(ad)+', 'add')
# print(m)    # ['ad']
# ret = re.search('(?P<id>\d{2})/(?P<name>\w{3})','23/com')
# print(ret.group())  # 23/com
# print(ret.group('id'))  # 23
# print(ret.group('name'))    # com

# ret = re.search('(?P<id>\d{3})', 'weeew34ttt123/ooo')
# print(ret.group())  # 123
# print(ret.group(('id')))

# ret = re.search('(?P<id>\d{3})/(?P<name>\w{3})','weeew34ttt123/ooo')
# print(ret.group())  # 123/ooo
# print(ret.group('id'))  # 123
# print(ret.group('name'))    # ooo



# match
# ret = re.match('asd', 'asdfhdsasd')
# print(ret)  # <re.Match object; span=(0, 3), match='asd'>
# print(ret.group())  # asd


# split
# ret = re.split('k', 'sadfskldj')
# print(ret)  # ['sadfs', 'ldj']


# ret = re.split('[j,s]', 'djksal')
# print(ret)  # ['d', 'k', 'al']


# sub
# ret = re.sub('a..x', 's..b', '123abcx456')
# print(ret)  # 123s..b456

# ret = re.sub('a..d', 's..........b', 'habcdfff')
# print(ret)  # hs..........bfff



# ret = re.findall('\.com', 'ddd.comaaa')
# print(ret)

# obj = re.compile('\.com')
# ret = obj.findall('aaa.combbb')
# print(ret)


# 注意： *  +  ? 等都是贪婪匹配，也就是尽可能匹配， 后面加?号使其变成惰性匹配
# ret = re.findall('abc*?', 'abccccc')
# print(ret)  # ['ab']


# ret = re.findall('a[bc]d', 'abcd')  # [bc]中括号里的bc是或的关系，只能取一个去匹配
# print(ret)  # []

# ret = re.findall('www.(\w+).com', 'www.baidu.com')
# print(ret)  # ['baidu']

# ret = re.findall('www.(?:\w+).com', 'www.baidu.com')
# print(ret)  # ['www.baidu.com']

# ret = re.sub('\d', 'abc', 'alvin5yuan6', 1)
# print(ret)  # alvinabcyuan6

# ret = re.finditer('\d', 'ds3sy4567a')
# print(next(ret))    # <re.Match object; span=(2, 3), match='3'>
# print(next(ret).group())    # 4
