# Project Overview
Open-CV-Metroid is on ongoing project to use [open-cv](https://opencv.org/) to find and track game elements within the [metroid](https://metroid.nintendo.com/) console game. 

# Project Dependencies
This project was run on a windows operating system and has not been tested in an OS enviornment. Several of the commands are windows specific. OS compatibility will be added shortly.
- Python 3.10
- Opencv-python 4.6.0.66
- numpy 1.23.2
- Pillow 9.2.0
- pywin32 304
- wheel 0.37.1
- pyAutoGui 0.9.53
- PyGetWindow 0.0.9

pythonwin packages for training the cascade
- Win32 gui, win32ui, win32con

## Code Structure 
- [main.py](https://github.com/Nkdiaz/Open-CV-Metroid/blob/master/main.py)
  - The main executable code to run, it loads the trained model from the cascade folder and does object detection. Also includes code to create screenshots to train cascade on different objects.
- [vision.py](https://github.com/Nkdiaz/Open-CV-Metroid/blob/master/vision.py)  
  - Contains the vision class, which includes gui window to adjust visual filters in real-time.
- [windowcapture.py](https://github.com/Nkdiaz/Open-CV-Metroid/blob/master/windowcapture.py)
  - Contains windowCapture class that takes a screenshot of window you want to capture.
- [edgefilter.py](https://github.com/Nkdiaz/Open-CV-Metroid/blob/master/edgefilter.py)
  - custom data structure to hold the state of a canny edge filter.

## Haar Cascade structure
The custom haar cascade was created using the [positive](https://github.com/Nkdiaz/Open-CV-Metroid/tree/master/positive) and [negative](https://github.com/Nkdiaz/Open-CV-Metroid/tree/master/negative) images of doors from the video game. The location of the images and their respective sizes are listed in the pos/neg.txt files. The trained cascade, parameters, and stages are kept in the [cascade](https://github.com/Nkdiaz/Open-CV-Metroid/tree/master/cascade) folder

# to run
Assumming all the dependencies are installed: 

The project is configured to capture and track the location of doors in real life while a user is playing the metroid video game. For the purposes of testing, there are several metroid speed run videos that were used to train the cascade. While they are not invoked in the main.py folder, there are several filters that could aid in object detection included in the project structure [hsv filter](https://github.com/Nkdiaz/Open-CV-Metroid/blob/master/hsvfilter.py) and [edge filter](https://github.com/Nkdiaz/Open-CV-Metroid/blob/master/edgefilter.py)

With a video of metroid playing in the background, run 'python main.py' which will invoke the haar cascade classifier and have object detection on the various doors encountered while playing. 




