#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 29 15:13:51 2023

@author: matsushimataichi
"""
import socket
import time
import random

def connect_unity(emotion):
    HOST = '127.0.0.1'
    PORT = 50007

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    while True:
        """
        a = random.randrange(3)
        result = str(a)
        print(a)
        client.sendto(result.encode('utf-8'),(HOST,PORT))
        time.sleep(2.0)
        """
        if (emotion == "fear"):
            message = str(emotion).encode('utf-8')
            client.sendto(message, (HOST,PORT))
        else:
            message = str(emotion).encode('utf-8')
            client.sendto(message, (HOST,PORT))
        time.sleep(1.0)
        