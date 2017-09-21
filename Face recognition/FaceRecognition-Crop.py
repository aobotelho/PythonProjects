'''
Created by: Andre Botelho
Date: Aug 2017
Based on: http://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html
'''

import cv2
import glob
import os

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
dataPath = './Images/Raw Images'
facesPath = './Images/Faces'

for docs in os.listdir('{}'.format(dataPath)):
    print('Getting Image: {}'.format(docs))
    try:
        coloredImage = cv2.imread('{}/{}'.format(dataPath,docs),cv2.IMREAD_COLOR)
        gray = cv2.cvtColor(coloredImage,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 5)

        for (x,y,w,h) in faces:
            face = gray[y:y+h,x:x+w]
            face = cv2.equalizeHist(face)
            cv2.imwrite('{}/{}'.format(facesPath,docs),face)

    except Exception as ex:
        print('Did not process {} correctly. Error: {}'.format(docs,ex))
