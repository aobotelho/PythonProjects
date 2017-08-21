'''
Created by: Andre Botelho
Date: Aug 2017
Based on: https://thecodacus.com/face-recognition-opencv-train-recognizer/#.WZoGr1SPJcY
Obs: Needs openCV 3.1 _contrib version
'''

import cv2
import glob
from PIL import Image
import os

#recognizer = cv2.createLBPHFaceRecognizer()

#Create user ID list
userList = []
for userID in os.listdir('./Images/Training Set/'):
    print('New user ID found: {}'.format(userID))
    userList.append(userID)

print('Final user ID list: {}'.format(userList))