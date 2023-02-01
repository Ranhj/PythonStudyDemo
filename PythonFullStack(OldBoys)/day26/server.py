# !/usr/bin/env python
# -*_ coding: utf-8 _*_
# Author:     Ran_hj
# Datetime:   2022-12-26 10:39
# className:  server.py
import socket

# family type

sk = socket.socket()
print(sk)
address = ('127.0.0.1', 8000)

sk.bind(address)

sk.listen(3)
print('waiting...')

# inp = input('>>>')
# conn.send(bytes(inp, 'utf8'))

while 1:
    conn, addr = sk.accept()
    print(addr)

    while 1:
        data = conn.recv(1024)

        # if not data:break
        if not data:
            conn.close()
            conn, addr = sk.accept()
            print(addr)
            continue
        print('.........', str(data, 'utf8'))
        inp = input('>>>')
        conn.send(bytes(inp, 'utf8'))


sk.close()