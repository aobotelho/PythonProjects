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
gotFrame = True
while(gotFrame):
    print('New Frame! Random string: ' + str(random.randint(0,10000)))
    gotFrame,frame = frames.read()

    cv2.imwrite('./tempVideo/{}.jpg'.format(str(counter)),frame)
    counter +=1
    '''try:
        ret,frame = frames.read()

        gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.2, 5)
        for (x,y,w,h) in faces:
            face = gray[y:y+h,x:x+w]
            face = cv2.equalizeHist(face)
            cv2.imwrite('{}/{}.jpg'.format(facesPath,str(random.randint(0,10000))),face)

    except Exception as ex:
        print('Did not process frame correctly. Error: {}'.format(ex))
    '''
frames.release()
cv2.destroyAllWindows()


print('done')