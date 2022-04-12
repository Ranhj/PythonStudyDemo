# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Rhj
# Datetime:   2022/3/14 10:39
# IDE:        PyCharm
# Title:      func_studentsOS_demo.py
# 学生管理系统

def main_interface():
    '''功能主界面'''
    print('请选择功能：')
    print('1.添加学员')
    print('2.删除学员')
    print('3.修改学员')
    print('4.查询学员')
    print('5.显示所有学员')
    print('6.退出系统')
    print('-'*20)
    return

# 新建一个列表，等待存储所有学生的信息，存储的数据以字典的形式存入  [{'xx':'xxx'}, {'xx':'xxxx'}]
info = []

def add_info():
    '''添加学生函数'''
    # 1.用户输入学生相关信息
    new_name = input('请输入要添加的学生姓名：')
    new_id = input('请输入要添加的学生学号：')
    new_tel = input('请输入要添加的学生电话：')

    # 2.判断是否添加这个学生：如果学生姓名已经存在就报错提示；如果不存在则添加数据
    global info
    # 2.1 不允许姓名重复，判断用户输入的姓名 和 列表里面字典的name对应的值， 相等 就提示
    for i in info:
        if new_name == i['name']:
            print('该学生已存在系统！')
            return
    # 2.2 如果输入的姓名不存在，则添加数据；准备空字典，字典新增数据，列表追加字典
    else:
        # 如果用户输入的姓名不存在，则添加该学生信息
        # 准备空字典
        info_dict = {}
        info_dict['name'] = new_name
        info_dict['id'] = new_id
        info_dict['tel'] = new_tel
        # 列表追加数据：   将这个学生的字典数据追加到列表
        info.append(info_dict)
        print(info)

def del_info():
    '''删除学生函数'''
    # 1.用户输入要删除的学生的姓名
    del_name = input('请输入要删除的学生姓名：')
    global info
    # 2.判断该学生是否存在：如果存在则删除，否则就报错
    for i in info:
        if del_name == i['name']:
            is_del = input('确认是否删除：yes OR no:\n')
            if is_del == 'yes':
                info.remove(i)
                print('删除成功！')
            elif is_del == 'no':
                break
            else:
                print('输入有误！请重新输入！')
            break
    else:
        print('该学生不存在')

    print(info)


def modify_info():
    '''修改学生信息函数'''
    # 1.用户输入要修改的学生的姓名
    modify_name = input('请输入要修改的学生姓名：')
    global info
    # 2.判断该学生是否存在：存在则修改信息，否则报错
    for i in info:
        if modify_name == i['name']:
            # new_id = input('请输入新学号：')
            # i['id'] = new_id
            i['id'] = input('请输入新学号：')  # 可以直接接收

            # new_tel = input('请输入新电话号码：')
            # i['tel'] = new_tel
            i['tel'] = input('请输入新手机号码：')
            break
    else:
        print('该学生不存在')

    print(info)

def search_info():
    '''查询学生函数'''
    # 1.输入要查找的学生姓名
    search_name = input('请输入要查询的学生姓名：')

    # 2.判断该学生是否存在：存在则显示该学生相应信息；否则就报错提示
    # 2.1 声明info为全局变量
    global info
    # 2.2 遍历info，判断输入的学生是否存在
    for i in info:
        if search_name == i['name']:
            # 如果该学生存在，则打印信息并使用break终止for循环
            print('查找到的学生信息如下----------：')
            print(f"该学生的姓名是{i['name']}, 学号是{i['id']}, 电话号码是{i['tel']}")
            break
    else:
        # 如果该学生不存在，给出提示
        print('查无此人！')

def print_all():
    '''显示所有学生信息'''
    # 1.打印title
    print("姓名\t\t\t\t学号\t\t\t\t电话号码")   # 制表符占位，为了对齐好看
    # 2.遍历打印所有学生的信息
    for i in info:
        print(f"{i['name']}\t\t\t\t{i['id']}\t\t\t\t{i['tel']}")



while True:
    # 1.显示功能主界面
    main_interface()
    # 2.用户输入功能序号
    use_num = input('请输入要使用功能的序号：')
    # 3.按照用户输入的功能序号，执行不同的功能（函数） 多重判断
    if use_num == '1':
        add_info()
    elif use_num == '2':
        del_info()
    elif use_num == '3':
        modify_info()
    elif use_num == '4':
        search_info()
    elif use_num == '5':
        print_all()
    elif use_num == '6':
        # 程序要想结束，退出终止while True --break
        exit_flag = input('确定要退出系统吗？ yes  OR  no：\n')
        if exit_flag == 'yes':
            break
        elif exit_flag == 'no':
            continue
        else:
            print('输入有误！请重新输入：')
    else:
        print('对不起！您输入有误，请重新输入：')
