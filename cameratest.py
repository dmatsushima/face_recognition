#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 22 15:41:53 2023

@author: matsushimataichi
"""
import cv2

cap = cv2.VideoCapture(1)

while(True):
    ret, frame = cap.read()
    
    cv2.imshow("frame",frame)
    
    k = cv2.waitKey(1) & 0xFF
    
    if k == ord("q"):
        break
    
cap.release()
cv2.destroyAllWindows()