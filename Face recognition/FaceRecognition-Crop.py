'''
Created by: Andre Botelho
Date: Aug 2017
Based on: http://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html
'''

import cv2
import glob
import random

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
dataPath = './Images/Raw Images'
facesPath = './Images/Faces'

for docs in glob.glob('{}/*.jpg'.format(dataPath)):
    coloredImage = cv2.imread(docs,cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(coloredImage,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.05, 5)

    for (x,y,w,h) in faces:
        face = coloredImage[y:y+h,x:x+w]
        #face = cv2.equalizeHist(face)
        cv2.imwrite('{}/{}.jpg'.format(facesPath,str(random.randint(0,5000))),face)
