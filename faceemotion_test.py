#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 21 23:46:29 2023

@author: matsushimataichi
"""
import cv2
import matplotlib.pyplot as plt
from deepface import DeepFace

img_path = cv2.imread(r'woman.jpg')
#print(img_path)

result = DeepFace.analyze(img_path= img_path ,actions=['emotion'], enforce_detection=False)
emotion = result['dominant_emotion']
print(result)
print(emotion)