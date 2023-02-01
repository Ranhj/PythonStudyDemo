# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-12-26 10:39
# className:  client.py
import socket

sk = socket.socket()
print(sk)
address = ('127.0.0.1', 8000)
sk.connect(address)

# data = sk.recv(1024)    # 阻塞
# data = sk.send(bytes('hah', 'utf8'))    # 阻塞

while True:
    inp = input('>>>')
    if inp == 'exit':
        break
    sk.send(bytes(inp, 'utf8'))
    # sk.send(bytes('yyy', 'utf8'))
    data = sk.recv(1024)
    print(str(data, 'utf8'))

# print(str(data, 'utf8'))

sk.close()