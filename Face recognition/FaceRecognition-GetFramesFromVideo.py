'''
Created by: Andre Botelho
Date: Aug 2017
Based on: http://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html
'''

import cv2
import glob
import os
import random

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
dataPath = './'
facesPath = './Images/Faces'

frames = cv2.VideoCapture('videoFaces.mp4')
counter=0
ret = 1
while(ret):
    print('New Frame!')
    ret,frame = frames.read()
    #cv2.imwrite('./tempVideo/{}.jpg'.format(str(counter)),frame)
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    for (x,y,w,h) in faces:
        face = gray[int(round(0.8*y)):int(round(0.8*(y+h))),int(round(0.8*x)):int(round(0.8*(x+w)))]
        face = cv2.equalizeHist(face)
        cv2.imwrite('{}/{}.jpg'.format(facesPath,str(counter)),face)
        counter +=1

frames.release()
cv2.destroyAllWindows()

print('done')