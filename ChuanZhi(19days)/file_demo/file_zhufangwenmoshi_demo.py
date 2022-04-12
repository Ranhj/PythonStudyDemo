# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/16 15:41
# IDE:        PyCharm
# Title:      file_zhufangwenmoshi_demo.py
"""
    r 读：如果文件不存在，会报错；不支持写入操作。
    读取时，文件指针在开头，所以能读取出来数据
"""
# f = open('test.txt', 'r')   # FileNotFoundError: [Errno 2] No such file or directory: 'test.txt'
# 在 r 模式下，对已有文件进行写入操作，会报错；不支持写入操作，表示只读
# f = open('file2.txt', 'r')
# f.write('Hi')       # io.UnsupportedOperation: not writable
# f.close()
import tarfile

"""
    w 只写：如果文件不存在，新建文件；执行写入，会覆盖现有内容。
    文件指针在开头，会用新内容覆盖原内容，就算不写入数据，他也会默认写入一个空数据，覆盖现有数据
"""
# f = open('file3.txt', 'w')  # file3.txt文件并不存在，所以新建了一个
# # f.write('AAA')    # 先写入AAA
# f.write('BBB')      # 再写入BBB，BBB会覆盖之前写入的AAA
# f.close()


"""
    a 追加：如果文件不存在，新建文件
    文件指针在末尾，所以无法读取数据（文件指针后面没有数据）
"""
# f = open('file4.txt', 'a')  # file4.txt文件并不存在，所以是新建了一个
# # f.write('aaa')    # 先写入aaa
# f.write('bbb')      # 再写入bbb,发现文件里展示的是aaabbb，所以是在上一次的基础上进行了追加操作
# f.close()


"""
    访问模式：
        访问模式参数可以省略，如果省略则表示访问模式为 r
"""
# f = open('file5.txt')   # file5.txt文件不存在，所以报错了：FileNotFoundError: [Errno 2] No such file or directory: 'file5.txt'
f = open('file4.txt')   # 访问的file4.txt文件存在，能正常访问
f.close()