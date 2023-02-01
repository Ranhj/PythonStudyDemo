# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-12-23 15:53
# className:  lianxi15.py

class Teach:
    def __init__(self, name,age):
        self.name = name
        self.age = age
        self.salary = 1000

class Course:

    def __init__(self, name, cost, teacher):
        self.name = name
        self.teacher = teacher
        self.cost = cost

    def class_up(self):
        self.teacher.salary += self.cost



t1 = Teach('李杰' ,8)
t2 = Teach('烧饼', 9)
t3 = Teach('豆饼', 10)

c1 = Course('生理课', 1, t1)

print(c1.name)
print(c1.teacher.age)
print(c1.teacher.name)
print(c1.teacher.salary)

c1.class_up()

print(c1.teacher.salary)