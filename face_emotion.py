#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug  5 13:54:15 2021

@author: matsushimataichi
"""

import cv2
from deepface import DeepFace
from connect_unity import connect_unity

face_cascade = cv2.CascadeClassifier('./opencv/data/haarcascades/haarcascade_frontalface_alt2.xml')

cap = cv2.VideoCapture(1)

while True:
    ret,frame = cap.read()
    result = DeepFace.analyze(img_path = frame, actions=['emotion'], enforce_detection=False)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    faces = face_cascade.detectMultiScale(gray,1.1,4)
    
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),3)
        
    emotion = result['dominant_emotion']
    
    txt = str(emotion)
    
    
    cv2.putText(frame,txt,(50,50),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),3)
    cv2.imshow('frame',frame)
    connect_unity(emotion)
    
    if cv2.waitKey(1) & 0xff == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
