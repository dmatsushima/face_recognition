#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 15:48:38 2023

@author: matsushimataichi
"""
import cv2

for i1 in range(-5, 5): 
    cap1 = cv2.VideoCapture( i1, cv2.CAP_DSHOW )
    if cap1.isOpened(): 
        print("VideoCapture(", i1, ") : Found")
    else:
        print("VideoCapture(", i1, ") : None")
    cap1.release() 