'''
Created by: Andre Botelho
Date: Aug 2017
Based on: https://thecodacus.com/face-recognition-opencv-train-recognizer/#.WZoGr1SPJcY
openCV Version: 3.1_contrib (installed on ubuntu 14.04 using https://github.com/rragundez/PyData/blob/master/Installation%20Steps%20for%20OpenCV%203.1.0.md)
'''

import cv2
import cv2.face
import numpy as np
import os

recognizer = cv2.face.createLBPHFaceRecognizer()

dataPath = './Images/Training Set'

IDs = []
userList = {}
faceList = []
for userID in os.listdir(dataPath):
    print('New user found: {}'.format(userID))
    userList[str(len(userList)+1)] = userID
    for faceSample in os.listdir('{}/{}/'.format(dataPath,userID)):
        IDs.append(len(userList))
        img = cv2.imread('{}/{}/{}'.format(dataPath,userID,faceSample),cv2.IMREAD_GRAYSCALE)
        faceList.append(img)

#Training uses np.array as IDs input
IDs = np.array(IDs)

with open('userIDS.txt','w') as file:
    file.write(str(userList))

recognizer.train(faceList,IDs)
recognizer.save('TrainedModel.yml')

#Finished!
print('Finished Training!!')