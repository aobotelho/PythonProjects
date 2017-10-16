'''
Created by: Andre Botelho
Date: Aug 2017
Based on: http://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html
Windows problem: 
    - https://stackoverflow.com/questions/46017894/python-2-7-and-opencv-3-3
    - https://github.com/opencv/opencv_contrib/issues/1267
'''

import cv2
import glob

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('TrainedModel.yml')

expPerc = 0.05

userID = eval(open('userIDS.txt','r').read())
print('User IDs read from file: ' + str(userID))

frames = cv2.VideoCapture(0)

while(frames.isOpened()):
    ret,coloredImage = frames.read()
    gray = cv2.cvtColor(coloredImage,cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.2, 5)
    for (x,y,w,h) in faces:
        face = gray[int(round((1-expPerc)*y)):int(round((1+expPerc)*(y+h))),int(round((1-expPerc)*x)):int(round((1+expPerc)*(x+w)))]
        face = cv2.equalizeHist(face)
        predictID = recognizer.predict(face)
        
        cv2.rectangle(coloredImage,(int(round((1-expPerc)*x)),int(round((1-expPerc)*y))),(int(round((1+expPerc)*(x+w))),int(round((1+expPerc)*(y+h)))),(0,255,0))

        if predictID[1] > 0:
            print('ID found: {}'.format(str(predictID[0])))
            
            cv2.putText(\
            coloredImage,\
            'ID: {} ... confidence: {}'.format(userID[str(predictID[0])],str(predictID[1])),\
            (x,y),\
            cv2.FONT_HERSHEY_SIMPLEX,0.5,(0,255,0))

    cv2.imshow('Image',coloredImage)
    if cv2.waitKey(1) == ord('q'):
        break
cv2.destroyAllWindows()
print('Finished!!')
