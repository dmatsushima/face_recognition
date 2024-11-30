#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  8 14:20:58 2021

@author: matsushimataichi
"""
import pybullet as p
import time
import pybullet_data

##############################
# シミュレータ基本設定
##############################
#物理シミュレーターに接続
physicsClient = p.connect(p.GUI)

# データのある場所を登録
p.setAdditionalSearchPath(pybullet_data.getDataPath()) #optionally

# 重力を設定
p.setGravity(0,0,-10)

##############################
# モデルを読み込み
##############################
# 地面を用意
planeId = p.loadURDF("plane.urdf")

# ロボットモデルを用意
carId = p.loadURDF("racecar/racecar.urdf", basePosition=[0,0,0.2])

################################
# シミュレーションループ
################################
for i in range (1000):
    p.stepSimulation()
    time.sleep(1./240.)

# 現在の状態を取得
cubePos, cubeOrn = p.getBasePositionAndOrientation(carId)
print(cubePos,cubeOrn)

#################################
# シミュレーション終了
#################################
p.disconnect()