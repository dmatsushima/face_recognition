#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 13 02:34:05 2021

@author: matsushimataichi
"""
import requests
import json, urllib
import time
import numpy as np
import cv2
from datetime import datetime
import matplotlib.pyplot as plt
import pandas as pd
#from pdb import set_trace
##初期設定
cap=cv2.VideoCapture(0) #0にするとmacbookのカメラ、1にすると外付けのUSBカメラにできる
csv_name = datetime.now().strftime('%Y%m%d_%H%M')#csvファイルとして保存するファイル名
data_name = ["anger","contempt","disgust","fear","happiness",'sadness','surprise']#保存データの系列
emotion_data =[0,0,0,0,0,0,0]#初期値
count = 0#撮影回数を示すカウンタ

##顔認識の設定
cascade_path =  '/Users/matsushimataichi/opencv/data/haarcascades/haarcascade_frontalface_alt2.xml'
cascade = cv2.CascadeClassifier(cascade_path)

##Faceの設定
subscription_key = '3a88bcfbef474fe4a093baa4fe8ca280'#ここに取得したキー１を入力
assert subscription_key
face_api_url = 'https://labkadai-1.cognitiveservices.azure.com/face/v1.0/detect'#ここに取得したエンドポイントのURLを入力

##実行
while True:
    r, img = cap.read()
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)#グレースケールに変換
    faces=cascade.detectMultiScale(img_gray, scaleFactor=1.1, minNeighbors=1, minSize=(100, 100))#顔判定 minSizeで顔判定する際の最小の四角の大きさを指定できる。(小さい値を指定し過ぎると顔っぽい小さなシミのような部分も判定されてしまう。)

    if len(faces) > 0: #顔を検出した場合
        for face in faces:
            now = datetime.now()#撮影時間
            filename = str(now)+'.jpg'#保存するfilename
            cv2.imwrite(filename, img)#画像の書き出し

            image_data = open(filename, "rb").read()#処理をする画像を選択
            headers = {'Ocp-Apim-Subscription-Key': subscription_key,
                       'Content-Type': 'application/octet-stream'}
            #params = {
                #'returnFaceId': 'true',
                #'returnFaceLandmarks': 'false',
                #'returnFaceAttributes': 'age,gender,headPose,smile,facialHair,glasses,emotion,hair,makeup,occlusion,accessories,blur,exposure,noise',
                #}
                
            params = {
                'returnFaceId': 'true',
                'returnFaceAttributes': 'emotion'
                }
            response = requests.post(face_api_url, headers=headers,
                                        params=params, data=image_data)#FaceAPIで解析
            
            #set_trace()

            #response.raise_for_status()
            analysis = response.json()#json出力

            #faceのjsonから抽出する項目をピック
            result = [analysis[0]['faceAttributes']['emotion']['anger'],analysis[0]['faceAttributes']['emotion']['contempt'],
                        analysis[0]['faceAttributes']['emotion']['disgust'],analysis[0]['faceAttributes']['emotion']['fear'],
                        analysis[0]['faceAttributes']['emotion']['happiness'],analysis[0]['faceAttributes']['emotion']['sadness'],
                        analysis[0]['faceAttributes']['emotion']['surprise']]

            emotion_data = np.array(result) + np.array(emotion_data)

            df = pd.DataFrame({now:emotion_data},
                            index=data_name)#取得データをDataFrame1に変換しdfとして定義

            if count == 0:#初期
                print(df)
            else:
                df = pd.concat([df_past,df],axis = 1, sort = False)#dfを更新
                print(df)

            plt.plot(df.T)#dfの行列を反転
            plt.legend(data_name)#凡例を表示
            plt.draw()#グラフ描画
            plt.pause(4)#ウェイト時間（=Azure更新時間）
            plt.cla()#グラフを閉じる

            count = count + 1#撮影回数の更新
            df_past = df#df_pastを更新

            df.T.to_csv(csv_name+'.csv')#感情分析結果をcsvファイルとして書き出し