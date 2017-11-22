'''
Created by: Andre Botelho
Date: Nov 2017
Needs opencv_contrib to work
'''

import cv2
import cv2.face
import numpy as np
import os
from random import randint

recognizer = cv2.face.LBPHFaceRecognizer_create()

trainingSetPath = './Images/Training Set'
testingSetPath = './Images/Testing Set'
rawImagesPath = './Images/Raw Images'
facesPath = './Images/Faces'

if not os.path.exists(trainingSetPath):
    os.makedirs(trainingSetPath)
if not os.path.exists(testingSetPath):
    os.makedirs(testingSetPath)
if not os.path.exists(rawImagesPath):
    os.makedirs(rawImagesPath)
if not os.path.exists(facesPath):
    os.makedirs(facesPath)

menuOptions = { '1': {'menu': 'Train Model','function':'trainModel'},
                '2': {'menu': 'Crop Faces From Images','function':'cropFromImages'},
                '3': {'menu': 'Crop Faces From Stored Video','function':'cropFromVideo'},
                '4': {'menu': 'Crop Faces From Live Video','function':'cropFromLiveVideo'},
                '5': {'menu': 'Recognize From Stored Video','function':'recognizeVideo'},
                '6': {'menu': 'Recognize From Stored Pictures','function':'recognizePicture'},
                '7': {'menu': 'Recognize From Live Video','function':'recognizeLive'},
                '8': {'menu': 'Send Faces to Training Folder','function':'facesToTrainingFolder'},
                '9': {'menu': 'Exit','function':'exit'}
                }

class FaceRecognition():
    def __init__(self):
        self.extraMargin = 0.05
        self.userListFileName = 'userIDS.txt'
        self.trainedModelFileName = 'TrainedModel.yml'
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

        self.recognizer = cv2.face.LBPHFaceRecognizer_create()
        if os.path.exists(self.trainedModelFileName):
            self.recognizer.read(self.trainedModelFileName)

        if os.path.exists(self.userListFileName):
            self.userList = open(self.userListFileName,'r').read()
            self.userList = eval(self.userList) if self.userList is not '' else {}
        else:
            self.userList = {}
            open(self.userListFileName,'w').close()
        pass

    def cropFromImages(self):
        '''
        This function gets all the images in the rawImagesPath folder, crop faces and store in facesPath folder
        '''
        for image in os.listdir(rawImagesPath):
            print('Cropping faces from image {}'.format(image))
            coloredImage = cv2.imread('{}/{}'.format(rawImagesPath,image),cv2.IMREAD_COLOR)
            gray = cv2.cvtColor(coloredImage,cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.1, 5)

            for (x,y,w,h) in faces:
                face = coloredImage[int(round((1-self.extraMargin)*y)):int(round((1+self.extraMargin)*(y+h))),
                int(round((1-self.extraMargin)*x)):int(round((1+self.extraMargin)*(x+w)))]
                cv2.imwrite('{}/{}'.format(facesPath,image),face)
        pass

    def facesToTrainingFolder(self):
        '''
        This function gets all the images on facesPath and stores them in traingSetPath in the proper folder
        The images on facesPath folder should be in the following format: {ID} - {randomNumberOrString}.png
        '''
        for image in os.listdir(facesPath):
            userID = image.split(' - ')[0]
            if userID not in self.userList:
                print('New User: {}'.format(userID))
                self.userList[userID] = str(len(self.userList))
                open(self.userListFileName,'w').write(str(self.userList))

            if not os.path.exists('{}/{}'.format(trainingSetPath,userID)):
                os.makedirs('{}/{}'.format(trainingSetPath,userID))

            os.rename('{}/{}'.format(facesPath,image),'{}/{}/{}'.format(trainingSetPath,userID,image))

        pass

    def cropFromVideo(self):
        '''
        Crops image from live video (Webcam probably?)
        '''
        singleUser = input('\nOk, I will crop face from video Now.\nWill there me only one user? (y/n): ')
        if singleUser == 'y' or singleUser == 'Y':
            singleUser = True
        else:
            singleUser = False
        singleUser == True if singleUser == ('y' or 'Y') else False
        userID = ''
        if singleUser == True:
            while userID == '':
                userID = input('Ok! What is the user name? ')

            if userID not in self.userList:
                self.userList[userID] = str(len(self.userList))
                open(self.userListFileName,'w').write(str(self.userList))
            if not os.path.exists('{}/{}'.format(trainingSetPath,userID)):
                os.mkdir('{}/{}'.format(trainingSetPath,userID))

        else:
            print('Ok, multiple faces will be detected. I will store it in the Faces folder\n\n')

        while True:
            videoName = input('What is the name of the video that you want me to get? ')
            if not os.path.exists(videoName):
                print('Video not found!')
            else:
                break
        frames = cv2.VideoCapture(videoName)
        ret = 1
        while(ret):
            ret,frame = frames.read()
            if not ret:
                break
            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.1, 5)
            for (x,y,w,h) in faces:
                face = frame[int(round((1-self.extraMargin)*y)):int(round((1+self.extraMargin)*(y+h))),
                            int(round((1-self.extraMargin)*x)):int(round((1+self.extraMargin)*(x+w)))]
                if singleUser == True:
                    cv2.imwrite('{}/{}/{} - {}.png'.format(trainingSetPath,userID,userID,str(randint(0,10000))),face)
                else:
                    cv2.imwrite('{}/{}.png'.format(facesPath,str(randint(0,10000))),face)
        frames.release()
        cv2.destroyAllWindows()

        print('done')
        pass

    def cropFromLiveVideo(self):
        '''
        Crops image from live video (Webcam probably?)
        '''
        singleUser = input('\nOk, I will crop face from video Now.\nWill there me only one user? (y/n): ')
        if singleUser == 'y' or singleUser == 'Y':
            singleUser = True
        else:
            singleUser = False
        userID = ''
        if singleUser == True:
            while userID == '':
                userID = input('Ok! What is the user name? ')

            if userID not in self.userList:
                self.userList[userID] = str(len(self.userList))
                open(self.userListFileName,'w').write(str(self.userList))
            if not os.path.exists('{}/{}'.format(trainingSetPath,userID)):
                os.mkdir('{}/{}'.format(trainingSetPath,userID))

        else:
            print('Ok, multiple faces will be detected. I will store it in the Faces folder\n\n')

        frames = cv2.VideoCapture(0)
        ret = 1
        while(ret):
            ret,frame = frames.read()

            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.1, 5)
            for (x,y,w,h) in faces:
                face = frame[int(round((1-self.extraMargin)*y)):int(round((1+self.extraMargin)*(y+h))),
                            int(round((1-self.extraMargin)*x)):int(round((1+self.extraMargin)*(x+w)))]
                if singleUser == True:
                    cv2.imwrite('{}/{}/{} - {}.png'.format(trainingSetPath,userID,userID,str(randint(0,10000))),face)
                else:
                    cv2.imwrite('{}/{}.png'.format(facesPath,str(randint(0,10000))),face)

                cv2.rectangle(frame,(int(round((1-self.extraMargin)*x)),int(round((1-self.extraMargin)*y))),(int(round((1+self.extraMargin)*(x+w))),int(round((1+self.extraMargin)*(y+h)))),(0,255,0))

            cv2.imshow('Video',frame)
            if cv2.waitKey(1) == ord('q'):
                break
        frames.release()
        cv2.destroyAllWindows()

        print('done')
        pass

    def trainModel(self):
        '''
        Here all the images on traingSetPath will be used to train the model
        '''
        IDs = []
        faceList = []

        for userFolder in os.listdir(trainingSetPath):
            print('Getting in user ID: {}'.format(userFolder))
            if userFolder not in self.userList:
                self.userList[userFolder] = str(len(self.userList))
                open(self.userListFileName,'w').write(str(self.userList))

            for faceSample in os.listdir('{}/{}'.format(trainingSetPath,userFolder)):
                IDs.append(int(self.userList[userFolder]))
                img = cv2.imread('{}/{}/{}'.format(trainingSetPath,userFolder,faceSample),cv2.IMREAD_GRAYSCALE)
                img = cv2.resize(img,(200,200), interpolation = cv2.INTER_CUBIC)
                img = cv2.equalizeHist(img)
                faceList.append(img)

        print('Read all faces. Now we are going to train the model')
        IDs = np.array(IDs)
        self.recognizer.train(faceList,IDs)
        self.recognizer.write(self.trainedModelFileName)

        print('Finished training model')
        pass

    def recognizeVideo(self):
        '''
        Recognize from stored video
        '''
        videoName = input('What is the name of the file?')
        frames = cv2.VideoCapture(videoName)
        ret = 1
        while(ret):
            ret,frame = frames.read()

            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.1, 5)
            for (x,y,w,h) in faces:
                face = frame[int(round((1-self.extraMargin)*y)):int(round((1+self.extraMargin)*(y+h))),
                            int(round((1-self.extraMargin)*x)):int(round((1+self.extraMargin)*(x+w)))]
                gray = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                gray = cv2.resize(gray,(200,200), interpolation = cv2.INTER_CUBIC)
                predictID = self.recognizer.predict(gray)

                cv2.rectangle(frame,(int(round((1-self.extraMargin)*x)),int(round((1-self.extraMargin)*y))),(int(round((1+self.extraMargin)*(x+w))),int(round((1+self.extraMargin)*(y+h)))),(0,255,0))

                foundName = ''
                for name,IDIndex in self.userList.items():
                    if str(IDIndex) == str(predictID[0]):
                        foundName = name
                cv2.putText(\
                frame,\
                'ID: {} - Confidence: {}'.format(foundName,predictID[1]),\
                (int(round((1-self.extraMargin)*x)),int(round((1-self.extraMargin)*y)) - 2),\
                cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,0))
            cv2.imshow('Video',frame)
            if cv2.waitKey(1) == ord('q'):
                break
        frames.release()
        cv2.destroyAllWindows()

        print('done')
        pass

    def recognizeLive(self):
        '''
        Real Time Recognition
        '''

        frames = cv2.VideoCapture(0)
        ret = 1
        while(ret):
            ret,frame = frames.read()

            gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, 1.1, 5)
            for (x,y,w,h) in faces:
                face = frame[int(round((1-self.extraMargin)*y)):int(round((1+self.extraMargin)*(y+h))),
                            int(round((1-self.extraMargin)*x)):int(round((1+self.extraMargin)*(x+w)))]
                gray = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                gray = cv2.resize(gray,(200,200), interpolation = cv2.INTER_CUBIC)
                predictID = self.recognizer.predict(gray)

                cv2.rectangle(frame,(int(round((1-self.extraMargin)*x)),int(round((1-self.extraMargin)*y))),(int(round((1+self.extraMargin)*(x+w))),int(round((1+self.extraMargin)*(y+h)))),(0,255,0))

                foundName = ''
                for name,IDIndex in self.userList.items():
                    if str(IDIndex) == str(predictID[0]):
                        foundName = name
                cv2.putText(\
                frame,\
                'ID: {} - Confidence: {}'.format(foundName,predictID[1]),\
                (int(round((1-self.extraMargin)*x)),int(round((1-self.extraMargin)*y)) - 2),\
                cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,0))
            cv2.imshow('Video',frame)
            if cv2.waitKey(1) == ord('q'):
                break
        frames.release()
        cv2.destroyAllWindows()

        print('done')
        pass

    def recognizePicture(self):
        '''
        Recognize pictures
        '''
        for testingFolders in os.listdir(testingSetPath):
            counter = 0
            for imageName in os.listdir('{}/{}'.format(testingSetPath,testingFolders)):
                frame = cv2.imread('{}/{}/{}'.format(testingSetPath,testingFolders,imageName))
                gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
                faces = self.face_cascade.detectMultiScale(gray, 1.1, 5)
                for (x,y,w,h) in faces:
                    face = frame[int(round((1-self.extraMargin)*y)):int(round((1+self.extraMargin)*(y+h))),
                                int(round((1-self.extraMargin)*x)):int(round((1+self.extraMargin)*(x+w)))]
                    gray = cv2.cvtColor(face,cv2.COLOR_BGR2GRAY)
                    gray = cv2.resize(gray,(200,200), interpolation = cv2.INTER_CUBIC)
                    predictID = self.recognizer.predict(gray)

                    cv2.rectangle(frame,(int(round((1-self.extraMargin)*x)),int(round((1-self.extraMargin)*y))),(int(round((1+self.extraMargin)*(x+w))),int(round((1+self.extraMargin)*(y+h)))),(0,255,0))

                    foundName = ''
                    for name,IDIndex in self.userList.items():
                        if str(IDIndex) == str(predictID[0]):
                            foundName = name
                    cv2.putText(\
                    frame,\
                    'ID: {} - Confidence: {}\nUser expected: {}'.format(foundName,predictID[1],testingFolders),\
                    (int(round((1-self.extraMargin)*x)),int(round((1-self.extraMargin)*y)) - 2),\
                    cv2.FONT_HERSHEY_SIMPLEX,0.8,(255,255,0))
                cv2.imshow('User: {} - {}'.format(testingFolders,str(counter)),frame)
                counter = counter + 1
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        print('done')
        pass

if __name__ == '__main__':
    recog = FaceRecognition()

    while(True):
        menuStr = 'Please select one option:\n'
        for menuitem in menuOptions:
            menuStr += '{}: {}\n'.format(menuitem,menuOptions[menuitem]['menu'])

        menuStr += '\nSelect: '
        currOpt = input(menuStr)

        if currOpt not in menuOptions:
            print('Sorry, I do not have option {}\n'.format(currOpt))
        elif menuOptions[currOpt]['function'] != 'exit':
            getattr(recog,menuOptions[currOpt]['function'])()
        else:
            input('Thanks for using me! Press enter to exit')
            break
