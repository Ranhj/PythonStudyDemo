# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-05-18 9:25
# className:  yield_weibingfa_demo.py
# yield伪并发
import time
def consumer(name):
    print("%s 准备吃包子啦！" % name)
    while True:
        baozi = yield

        print("包子[%s]来了，被[%s]吃了！" % (baozi, name))

def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦！")
    for i in range(10):
        time.sleep(1)
        print("做了2个包子！")
        c.send(i)
        c2.send(i)
producer("老子")

'''
A 准备吃包子啦！
B 准备吃包子啦！
老子开始准备做包子啦！
做了2个包子！
包子[0]来了，被[A]吃了！
包子[0]来了，被[B]吃了！
做了2个包子！
包子[1]来了，被[A]吃了！
包子[1]来了，被[B]吃了！
做了2个包子！
包子[2]来了，被[A]吃了！
包子[2]来了，被[B]吃了！
做了2个包子！
包子[3]来了，被[A]吃了！
包子[3]来了，被[B]吃了！
做了2个包子！
包子[4]来了，被[A]吃了！
包子[4]来了，被[B]吃了！
做了2个包子！
包子[5]来了，被[A]吃了！
包子[5]来了，被[B]吃了！
做了2个包子！
包子[6]来了，被[A]吃了！
包子[6]来了，被[B]吃了！
做了2个包子！
包子[7]来了，被[A]吃了！
包子[7]来了，被[B]吃了！
做了2个包子！
包子[8]来了，被[A]吃了！
包子[8]来了，被[B]吃了！
做了2个包子！
包子[9]来了，被[A]吃了！
包子[9]来了，被[B]吃了！
'''