#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 26 12:03:56 2021

@author: matsushimataichi
"""

import sys
import cv2


cap = cv2.VideoCapture(0)

if cap.isOpened() is False:
    print("can not open camera")
    sys.exit()

# 評価器を読み込み
# https://github.com/opencv/opencv/tree/master/data/haarcascades
cascade = cv2.CascadeClassifier('/Users/matsushimataichi/opencv/data/haarcascades/haarcascade_frontalface_alt2.xml')
#eye_cascade = cv2.CascadeClassifier('/Users/matsushimataichi/opencv/datahaarcascades/haarcascade_eye_tree_eyeglasses.xml')


while True:
    ret, frame = cap.read()

    # そのままの大きさだと処理速度がきついのでリサイズ
    frame = cv2.resize(frame, (int(frame.shape[1]*0.3), int(frame.shape[0]*0.3)))

    # 処理速度を高めるために画像をグレースケールに変換したものを用意
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 顔検出
    facerect = cascade.detectMultiScale(
        gray,
        scaleFactor=1.11,
        minNeighbors=3,
        minSize=(100, 100)
    )

    if len(facerect) != 0:
        for x, y, w, h in facerect:
            # 顔の部分(この顔の部分に対して目の検出をかける)
            #face_gray = gray[y: y + h, x: x + w]

            # くり抜いた顔の部分を表示(処理には必要ない。ただ見たいだけ。)
            #show_face_gray = cv2.resize(face_gray, (int(gray.shape[1]), int(gray.shape[0])))
            #cv2.imshow('face', show_face_gray)


            # 顔検出した部分に枠を描画
            cv2.rectangle(
                frame,
                (x, y),
                (x + w, y + h),
                (255, 255, 255),
                thickness=2
            )

    cv2.imshow('frame', frame)

    # キー入力を1ms待って、k が27（ESC）だったらBreakする
    k = cv2.waitKey(1)
    if k == 27:
        break

# キャプチャをリリースして、ウィンドウをすべて閉じる
cap.release()
cv2.destroyAllWindows()