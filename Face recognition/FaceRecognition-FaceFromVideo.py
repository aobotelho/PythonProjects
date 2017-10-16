'''
Created by: Andre Botelho
Date: Aug 2017
Based on: http://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html
'''

import cv2
import os
import random

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
dataPath = './'
facesPath = './Images/Faces'

expPerc = 0.05

frames = cv2.VideoCapture(0)
counter=0
ret = 1
while(ret):
    print('New Frame!')
    ret,frame = frames.read()
    
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    for (x,y,w,h) in faces:        
        face = gray[int(round((1-expPerc)*y)):int(round((1+expPerc)*(y+h))),int(round((1-expPerc)*x)):int(round((1+expPerc)*(x+w)))]
        #face = gray[y:y+h,x:x+w]
        face = cv2.equalizeHist(face)        
        cv2.imwrite('{}/{}.jpg'.format(facesPath,str(counter)),face)
        counter +=1

        #cv2.rectangle(frame,(int(round(0.8*y)),int(round(0.8*y))),(int(round(1.2*(x+w))),int(round(1.2*(y+h)))),(0,255,0))
        cv2.rectangle(frame,(int(round((1-expPerc)*x)),int(round((1-expPerc)*y))),(int(round((1+expPerc)*(x+w))),int(round((1+expPerc)*(y+h)))),(0,255,0))

    cv2.imshow('Video',frame)
    if cv2.waitKey(1) == ord('q'):
        break
frames.release()
cv2.destroyAllWindows()

print('done')