# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-04-12 17:07
# className:  shopping.py

product_list = [
    ("Mac", 9000),
    ("kindle", 800),
    ("tesla", 900000),
    ("pythonbook", 105),
    ("bike", 2000),
]
saving = input('please input your money：')
shopping_car = []

if saving.isdigit():
    saving = int(saving)
    while True:
        # 打印商品内容
        for i, v in enumerate(product_list, 1):
            print(i, '>>>>', v)

        # 引导用户选择商品
        choice = input('选择购买商品编号[退出：q]：')

        # 验证输入是否合法
        if choice.isdigit():
            choice = int(choice)
            if choice > 0 and choice <= len(product_list):
                # 将用户选择商品通过choice取出来
                p_item = product_list[choice-1]

                # 如果钱够，用本金saving减去该商品价格，并将该商品加入购物车
                if p_item[1] < saving:
                    saving -= p_item[1]

                    shopping_car.append(p_item)

                else:
                    print('余额不足，还剩%s' % saving)
                print(p_item)
            else:
                print('编码不存在')
        elif choice == 'q':
            print('-----------您已经购买如下商品-----------')
            # 循环遍历购物车里的商品，购物车存放的是已买商品
            for i in shopping_car:
                print(i)
            print('您还剩%s元钱' % saving)
            break
        else:
            print('invalid input')
