#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 10:57:16 2021

@author: matsushimataichi
"""
import requests,json,urllib.request,os
from PIL import Image,ImageDraw,ImageFont

subscription_key = "3a88bcfbef474fe4a093baa4fe8ca280"

face_api_url = "https://labkadai-1.cognitiveservices.azure.com/" + '/face/v1.0/detect'

image_url = 'https://upload.wikimedia.org/wikipedia/commons/3/37/Dagestani_man_and_woman.jpg'

headers = {'Ocp-Apim-Subscription-Key': subscription_key}

params = {
    'returnFaceId': 'true',
    'returnFaceAttributes': 'emotion'
}

response = requests.post(face_api_url, params=params,
                         headers=headers, json={"url": image_url})
print(json.dumps(response.json()))