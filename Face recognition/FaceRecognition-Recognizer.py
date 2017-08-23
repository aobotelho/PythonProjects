'''
Created by: Andre Botelho
Date: Aug 2017
Based on: http://docs.opencv.org/trunk/d7/d8b/tutorial_py_face_detection.html
'''

import cv2
import glob
import random

recognizer = cv2.face.createLBPHFaceRecognizer()
recognizer.load('TrainedModel.yml')

userID = eval(open('userIDS.txt','r').read())
print('User IDs read from file: ' + str(userID))

dataPath = './Images/Testing Set'

for docs in glob.glob('{}/*.jpg'.format(dataPath)):
    coloredImage = cv2.imread(docs,cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(coloredImage,cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    predictID = recognizer.predict(gray)
    print('ID found: {}'.format(userID[str(predictID)]))
    cv2.putText(\
    coloredImage,\
    'ID: {}'.format(userID[str(predictID)]),\
    (int(round(gray.shape[0]/10)),int(round(gray.shape[1]/10))),\
    cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,0))

    cv2.imshow(docs,coloredImage)

cv2.waitKey(0)
cv2.destroyAllWindows()
