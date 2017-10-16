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

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('TrainedModel.yml')

userID = eval(open('userIDS.txt','r').read())
print('User IDs read from file: ' + str(userID))

dataPath = './Images/Testing Set'
gotIt = 0
what = 0
for docs in glob.glob('{}/*/*.jpg'.format(dataPath)):
    coloredImage = cv2.imread(docs,cv2.IMREAD_COLOR)
    gray = cv2.cvtColor(coloredImage,cv2.COLOR_BGR2GRAY)
    gray = cv2.equalizeHist(gray)
    predictID = recognizer.predict(gray)
    if predictID[1] > 30:
        print('ID found: {}'.format(userID[str(predictID[0])]))
        cv2.putText(\
        coloredImage,\
        'ID: {}'.format(userID[str(predictID[0])]),\
        (int(round(gray.shape[0]/10)),int(round(gray.shape[1]/10))),\
        cv2.FONT_HERSHEY_SIMPLEX,0.5,(255,255,0))

        #cv2.imshow(docs,coloredImage)
        gotIt = gotIt + 1
    else:
        what = what + 1

cv2.waitKey(0)
cv2.destroyAllWindows()
print('Got: {} ; what: {}'.format(str(gotIt),str(what)))
print('Finished!!')
