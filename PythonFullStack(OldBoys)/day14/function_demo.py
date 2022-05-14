# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-05-06 16:32
# className:  function_demo.py
"""
  函 数
函数 != function()
计算机函数 == subroutine 子程序，procedures 过程

叫法：编程中的函数在英文中也有很多不同的叫法。在BASIC中叫做subroutine(子过程或子程序)，在Pascal中叫做procedure(过程)和function，在C中只有function，在Java里面叫做method

定义：函数是指将一组词句的集合通过一个名字(函数名)封装起来，要想执行这个函数，只需调用其函数名即可

作用：
    1.减少重复代码
    2.方便修改，更易扩展
    3.保持代码一致性

define：定义    def

格式：
def 函数名(参数列表)：
    函数体
调用：  函数名()   一定记得加括号，如果有形参必须传入相应个数的实参
命名规则：
    1.函数名必须以下划线或字母开头，可以包含任意字母、数字或下划线的组合。不能使用任何的标点符号
    2.函数名是区分大小写的
    3.函数名不能是保留字

形参和实参：
形参：形式参数，不是实际存在，是虚拟变量。在定义函数和函数体的时候使用形参，目的是在函数调用时接收实参(实参个数、类型应与实参一一对应)
实参：实际参数，调用函数时传给函数的参数，可以是常量、变量、表达式、函数。传给形参
区别：
    1.形参是虚拟的，不占用内存空间，形参变量只有在被调用时才会分配内存单元，而实参是一个变量，占用内存空间；
    2.数据传送单向，实参传给形参，不能形参传给实参
"""
# def add(a, b):
#     print(a + b)
# def jian(a, b):
#     print(a - b)
# def cheng(a, b):
#     print(a * b)
# def chu(a, b):
#     print(a / b)
#
# add(3, 5)
# jian(10, 4)
# cheng(3, 6)
# chu(12, 6)


# def add(b, a):  # 按顺序对应，且传入的实参必须与形参个数一致
#     print(f'a:{a}')
#     print(f'b:{b}')
# add(2, 3)
#
# def print_info(name, age, sex='男'):# 3.默认参数  sex='男' 是默认参数，没传入实参就给出默认参数，传了就是用传入的实参
#     print('Name: %s' % name)
#     print('Age: %s' % age)
#     print('Sex: %s' % sex)
#
# # 1.必须参数，位数要一一对应
# print_info('张三', 19)
# # 2.关键字参数
# print_info(age=20, name='李美', sex='女')

# 4.不定长参数
# def add(*args):
#     # print(args)
#     sum = 0
#     for i in args:
#         sum += i
#     print(sum)
# add(1)
# add(1, 2)
# add(1, 2, 3)
# add(1, 2, 3, 4)

# def print_info(*args, **kwargs):
#     # print(args) #   打印的是args的不指定参数 ('小张', 18, '男')
#     # print(kwargs)   # 打印的是kwargs的默认指定参数  {'job': 'IT', 'hobby': 'Guitar', 'height': 170}
#     for i in kwargs:
#         print('%s:%s'%(i,kwargs[i]))
#
# # print_info('小张', 18, '男', job='IT', hobby='Guitar', height=170)
# print_info( job='IT', hobby='Guitar', height=170)


# def f(*args, **kwargs):
#     pass
# f(1, 2, '23','Hello', [11, 22], name='lisi', age=19)

# 关于不定长参数的位置：*args放在左边，**kwargs参数放在右边，否则会报错
# 如果有默认参数，放左边
# def func(name, age=18, *args, **kwargs):
#     pass

# def f(**kwargs):
#     print(kwargs)
#
# # f(info={'name': "Lily"})    # {'info': {'name': 'Lily'}}
# f(**{'name': "Lily"})   # {'name': 'Lily'}  要想直接传入字典，可以在前面加上**



"""
    函数返回值
注意：
    1.函数在执行过程中只要遇到return语句，就会停止执行并返回结果，so也可以理解为return语句代表着函数的结束
    2.如果未在函数中指定return，那么这个函数的返回值为None
    3.return多个对象，解释器会把这多个对象组装成一个元组作为一个一个整体结果输出 
"""
# def f():
#     print('ok')
#     # return None
#     return 5    # return作用：1.结束函数  2.返回某个对象
#     print('Hello')  # 方法体内return下面的代码不会执行
# a = f()
# print(a)

"""
    函数作用域：
L：local，局部作用域，即函数中定义的变量
E：enclosing，嵌套的父级函数的局部作用域，即包含此函数的上级函数的局部作用域，但不是全局的
G：global，全局变量，就是模块级别定义的变量
B：built-in，系统固定模块里面的变量，比如int，bytearray等。
搜索变量的优先级顺序依次是：作用域局部 > 外层作用域 > 当前模块中的全局 > Python内置作用域，也就是LEGB

"""
# if True:
#     x = 3
# print(x)
#
# def f():
#     a = 10
# f()
# # print(a)  定义的a的作用域尽在函数内

# x = int(2.9)    # int built-in
# print(x)

# count = 10
# def outer():
#     global count  # global
#     print(count)
#     count = 5
#     print(count)
# outer()


# def outer():
#     count = 15      # 在enclosing这一层
#     def inner():
#         nonlocal count  # 用nonlocal修饰
#         count = 20
#         print(count)
#     inner()
#     print(count)
# outer()

'''
 python nonlocal 和 global 的区别
简单总结：
1）任何一层子函数，若直接使用全局变量且不对其改变的话，则共享全局变量的值；一旦子函数中改变该同名变量，则其降为该子函数所属的局部变量；
2）global可以用于任何地方，声明变量为全局变量（声明时，不能同时赋值）；声明后再修改，则修改了全局变量的值；
3）而nonlocal的作用范围仅对于所在子函数的上一层函数中拥有的局部变量，必须在上层函数中已经定义过，且非全局变量，否则报错。
nonlocal:
只在闭包里面生效，作用域就是闭包里面的，外函数和内函数都影响，但是闭包外面不影响。
nonlocal 语句使列出的标识符引用除global变量外最近的封闭范围中的以前绑定的变量。 这很重要，因为绑定的默认行为是首先搜索本地名称空间。 该语句允许封装的代码将变量重新绑定到除全局(模块)作用域之外的本地作用域之外。
'''


"""高阶函数"""
# def f(n):
#     return n * n
#
#
# def foo(a, b, func):
#     ret = func(a) + func(b)
#     return ret
# print(foo(3, 4, f))
#
#
# def bar(a, b, func):
#     # func()
#     return 1
# bar(1, 2, f)
#
# # 函数名可以进行赋值
# # 函数名可以作为函数参数，还可以作为函数的返回值



"""
    递归函数
关于递归：
    1.调用自身函数
    2.有一个结束条件
但凡是递归可以写的，循环都可以解决
递归的效率在很多时候会很低

函数都可以写成循环的方式，但循环的逻辑不如递归清晰
递归特性：
    1.必须有一个明确的结束条件
    2.每次进入更深一层递归时，问题规模相比上次递归都应有所减少
    3.递归效率不高，递归层次过多会导致栈溢出(在计算机中，函数调用是通过栈(stack)这种数据结构实现的，每当进入一个函数调用，
    栈就会加一层栈帧，每当函数返回，栈就会减一层栈帧。由于栈的大小不是无限的，所以，递归调用的次数过多，会导致栈溢出。)

"""
# 阶乘
# 1.用循环的方式
# def fat(n):
#     res = 1
#     for i in range(1, n+1):
#         res *= i
#     return res
# print(fat(7))

# 2.用递归的方式
# def fact(n):
#     if n == 1:
#         return 1
#     return n*fact(n-1)
#
# print(fact(5))

# 斐波那契数列：
# 这个数列从第3项开始，每一项都等于前两项之和：0 1 1 2 3 5 8 13 21 34 55 ...
# def fibo(n):
#     before = 0
#     after = 1
#     for i in range(n-1):
#         ret = before+after
#         before = after
#         after = ret
#     return ret
# print(fibo(9))  # 34
# print(fibo(10))  # 55
#
#
# def fibo2(n):
#     if n <= 1:
#         return 1
#     return fibo2(n-1) + fibo2(n-2)
# print(fibo2(9))  # 55
# print(fibo2(10))  # 89

# # eval() 可以直接计算
# print(eval('3+2*8'))
# print(eval('2**32'))

# str = ['a', 'b', 'c', 'd']
# def fun1(s):
#     if s != 'a':
#         return s
# ret = filter(fun1, str)  # ['b', 'c', 'd']
# print(ret)  # <filter object at 0x0000022551556BB0>
# print(list(ret))    # ret是一个迭代器对象

# str = ['a', 'b', 'c', 'd']
# def fun2(s):
#     return s + "Hello"
# ret = map(fun2, str)    # if ret = map(fun2, str) 注意filter与map的区别
# print(ret)  # <map object at 0x00000182C16E6BB0>  map object的迭代器
# print(list(ret))    # ['aHello', 'bHello', 'cHello', 'dHello']



# reduce
# from functools import reduce
# def add1(x,y):
#     return x + y
# print(reduce(add1, range(1,101)))   # 5050     reduce 的结果就是一个值

"""
匿名函数：lambda
匿名函数的命名规则，用lambda关键字标识，冒号(:)左侧表示函数接收的参数(a,b)，冒号(:)右侧表示函数的返回值(a+b)
因为lambda在创建时不需要命名，所以叫匿名函数
"""

# add = lambda a, b: a+b
# print(add(2, 3))    # 5


"""函数式编程"""
# 求阶乘：通过reduce函数加lambda表达式实现阶乘非常简单
from functools import reduce
print(reduce(lambda x, y: x*y, range(1, 6)))
# map()函数加上lambda表达式(匿名函数)可以实现更强大的功能
squares = map(lambda x: x*x, range(9))
print(squares)  # <map object at 0x0000017709BB6BB0> 迭代器
print(list(squares))    # [0, 1, 4, 9, 16, 25, 36, 49, 64]
