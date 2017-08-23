'''
Created by: Andre Botelho
Date: Aug 2017
Based on: http://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html
'''

import cv2
import glob
import random

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

for docs in glob.glob('./Images/Raw Images/*.jpg'):
    gray = cv2.imread(docs,cv2.IMREAD_GRAYSCALE)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    for (x,y,w,h) in faces:
        face = gray[y:y+h,x:x+w]
        face = cv2.equalizeHist(face)
        cv2.imwrite('./Images/Faces/{}.jpg'.format(str(random.randint(0,1000))),face)
