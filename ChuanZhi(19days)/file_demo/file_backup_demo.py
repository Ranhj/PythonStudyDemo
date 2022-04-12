# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/17 14:20
# IDE:        PyCharm
# Title:      file_backup_demo.py

# 文件备份
# 1.用户输入目标文件    举例：sound.txt.mp3
old_name = input('请输入您要备份的文件名：')
# print(type(old_name))   # <class 'str'>
print(old_name)             # sound.txt.mp3

# 2.规划备份文件的名字
# 2.1 提取后缀  --找到名字中的点 --名字和后缀分离 --最右侧的点才是后缀的点 --字符串查找某个字串 rfind
index = old_name.rfind('.')     # 查找最右侧的点并返回左边的长度
print(index)                    # 9

# 2.2 组织新名字 = 原名字 + [备份] + 后缀
# 原名字就是字符串中的一部分子串   --切片[开始：结束：步长]
print(old_name[:index])         # 切片返回点左边下标的数据： sound.txt
print(old_name[index:])         # 切片返回点右边下标的数据： .mp3
new_name = old_name[:index] + "[备份]" + old_name[index:]     # 拼接
print(new_name)                 # sound.txt[备份].mp3

# 3.备份文件写入数据（数据和源文件一样）
# 3.1 打开 原文件 和 备份文件
old_f = open(old_name, 'rb')
new_f = open(new_name, 'wb')

# 3.2 原文件读取，备份文件写入
# 如果不确定目标文件大小，循环读取写入，当读取出来的数据没有了就终止循环
while True:
    content = old_f.read(1024)
    if len(content) == 0:   # 读取完了，就退出
        break
    new_f.write(content)

# 3.3 关闭文件
old_f.close()
new_f.close()


