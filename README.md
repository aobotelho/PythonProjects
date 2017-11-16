# PythonProjects
Repo with all my python projects

## Face Recognition
This folder contains my face recognition project using OpenCV. It was based on a lot of examples on the internet.
The script creates and expects certain files and folders in an specific format:
- On the root folder it will have:
    - FaceRecognition.py: The python file that runs the whole thing
    - haarcascade_frontalface_alt.xml: The file used to recognize faces
    - TrainedModel.yml: The file that will be created once the user trains the model
    - userIDS.txt: The file with the dict to map the predicted name and the ID the OpenCV finds.
    - Images folder: on this folder the images will be stored in a specific path and with a specific format.
        - Faces: This folder is where all the faces cropped from photos or video will be stored to further be moved to the right folder from training. Here the faces will be stored with a random integer as the name.
        - Raw Images: Folder that contains pictures with **just one** user. The file name format expected is:
            - {User Name} - {Random String}.{File Extension}
        - Testing Set: Folder that contains folders with all the user names you want to test your trained model, i.e. if you want to test pictures for Mark and Joe, in this folder there should be two folders named 'Mark' and 'Joe'. Within these folders the images should follow the same format as described above:
            - {User Name} - {Random String}.{File Extension}
        - Training folder: This folder contains all the training pictures. This folder follow the same format as described above on _Testing Set_ folder.
- The script opens up a menu with 9 options:
    1. Train Model: This option will get all the images in _Training Folder_ and traine a new model with that. The User Names it will detect are the names of the folders within training folder.
    2. Crop Faces From Images: This option will crop the faces it finds from the _Raw Images_ folder and store it in _Faces_ folder.
    3. Crop Faces From Stored Video: It will crop the faces it finds from all the frames in an stored video. The user should provide the path for the video and if it contains only one user or not. If it contains only one user the script will store the faces it finds on the _Training Folder_, otherwise it will store in the _Faces Folder_.
    4. Crop From Live Video: Same as above, but it will get images from users webcam.
    5. Recognize From Stored Video: This option will try to recognize users from stored videos, once the model is trained. The path for the video should be provided
    6. Recognize From Stored Pictures: This option will try to recognize the users from the pictures within _Testing Set_ folder.
    7. Recognize From Live Vide: This option will try to recognize the users from the webcam video.
    8. Send Faces to Training Folder: This option will get all the faces from _Faces_ folder and store them in the _Training Set_ folder. It expects the files to follow the same format as described earlier:
        - {User Name} - {Random String}.{File Extension}
    9. Quits the program.

## GoogleMaps folder
This folder contains a simple script to get time and distance estimation from Google Maps. It expects a file named Cities.csv and that follow the format according the file Cities_Model.csv:
    - ORIGIN_CITY: City of Origin
    - ORIGIN_STATE: State of Origin
    - DESTINATION_CITY: Destination City
    - DESTINATION_STATE: Destination State
    - HOURS: Total hours between both, to be completede by the script
    - MINUTES: Minutes between both excluding the full hours computaded above
    - TOTAL: Total time between both in decimal format, e.g. 1h 15min = 1,25h

The script will output a file named FullCities.csv.
The script expects a file named MapsKey.txt where the Google Maps API key should be stored. More on: https://developers.google.com/maps/documentation/javascript/get-api-key