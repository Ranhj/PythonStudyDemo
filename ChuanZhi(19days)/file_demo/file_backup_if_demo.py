# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/17 15:32
# IDE:        PyCharm
# Title:      file_backup_if_demo.py
# 需求：如果用户输入 .txt ，这是一个无效文件，程序如何更改才能限制只有输入有效的文件名才能备份？
#   添加条件判断  if
old_name = input('请输入你要备份的文件名：')
index = old_name.rfind('.')
print(index)

# 4.思考：有效文件才备份
if index > 0:
    # 提取后缀
    postfix = old_name[index:]
    print(postfix)
new_name = old_name[:index] + '[备份]' + postfix
print(new_name)

old_f = open(old_name, 'rb')
new_f = open(new_name, 'wb')

while True:
    content = old_f.read()
    if len(content) == 0:
        break
    new_f.write(content)
    print(content)

old_f.close()
new_f.close()