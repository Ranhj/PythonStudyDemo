# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/17 17:23
# IDE:        PyCharm
# Title:      file_batchrename_demo.py

# 批量重命名操作
# 需求1：把code文件夹所有文件重命名   Python_
# 需求2：删除前缀 Python_  重命名     1.构造条件的数据   2.书写if
import os

# 构造条件的数据
# flag=1:加前缀Python_
# flag=2:去掉前缀Python_
flag = 1

# 1.找到所有文件：获取a文件夹的目录列表 --listdir(路径+目录名)
# 先在'D:\\desktop\\a'路径下新建几个文件
file_list = os.listdir('D:\\desktop\\a')
os.chdir('D:\\desktop\\a')  # 切换到a目录
print(os.getcwd())          # 打印查看是否切换成功

# 2.构造名字
for i in file_list:
    if flag == 1:
        # new_name = 'Python_' + 原文件i
        new_name = 'Python_' + i
    elif flag == 2:
        # 删除前缀  切片去掉前缀
        num = len('Python_')
        new_name = i[num:]
# 3.重命名：这个一定要写道for循环里面，否则只更改一个，大意地踩了一次坑
    os.rename(i, new_name)
