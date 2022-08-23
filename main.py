import cv2 as cv
import numpy as np
import os
from time import time
from windowcapture import WindowCapture
from vision import Vision


# initialize the WindowCapture class
wincap = WindowCapture()

#load the trained model
cascade_door = cv.CascadeClassifier('cascade/cascade.xml')

vision_door = Vision(None)

loop_time = time()
while(True):

    # get an updated image of the game
    screenshot = wincap.get_screenshot()

    #do object detection
    rectangles = cascade_door.detectMultiScale(screenshot)

    #draw the detection results onto the origional image
    detection_image = vision_door.draw_rectangles(screenshot,rectangles)

    cv.imshow('matches', detection_image)

    # debug the loop rate
    print('FPS {}'.format(1 / (time() - loop_time)))
    loop_time = time()

    # press 'q' with the output window focused to exit.
    # press 'f' to save screenshot as a positive image, press 'd' to
    # save as a negative image.
    # waits 1 ms every loop to process key presses

    if cv.waitKey(1) == ord('q'):
        cv.destroyAllWindows()
        break
    elif cv.waitKey(1) == ord('f'):
        cv.imwrite('positive/{}.jpg'.format(loop_time), screenshot)
        print("positive")
    elif cv.waitKey(1) == ord('d'):
        cv.imwrite('negative/{}.jpg'.format(loop_time), screenshot)
        print("negative")

print('Done.')
