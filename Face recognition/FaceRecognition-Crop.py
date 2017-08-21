'''
Created by: Andre Botelho
Date: Aug 2017
Based on: http://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html
'''

import cv2
import glob
import random
from os import getcwd
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

for docs in glob.glob('./Images/Raw Images/*.jpg'):
    img = cv2.imread(docs)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)

    for (x,y,w,h) in faces:
        face = gray[y:y+h,x:x+w]
        face = cv2.equalizeHist(face)
        cv2.imwrite('./Images/Faces/{}.jpg'.format(str(random.randint(0,1000))),face)
