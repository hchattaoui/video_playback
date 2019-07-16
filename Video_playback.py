
# coding: utf-8

#!/usr/bin/env python


import cv2
import sys


try:
    video_file_path = str(sys.argv[1])
    fps = int(sys.argv[2])
    width = int(sys.argv[3])
    height = int(sys.argv[4])
    monochrome = (str(sys.argv[5]) == 'True')
except:
    video_file_path = 'video_1.mp4'
    fps = 100
    width = 1500
    height = 900
    monochrome = False

def play(video_file_path, fps, width, height, monochrome):
    cap = cv2.VideoCapture(video_file_path)
    ret, frame = cap.read()
    if (cap.isOpened()== False): 
        print("Error opening video stream or file")

    while(cap.isOpened()):
        prev_frame=frame[:]
        ret, frame = cap.read()

        cv2.namedWindow('frame',cv2.WINDOW_NORMAL)
        cv2.resizeWindow('frame', (width,height))

        if monochrome == True:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        if ret == True:
            cv2.imshow('frame',frame)
            key = cv2.waitKey(int((1/fps)*1000))

            if key == ord('p'):
                key = cv2.waitKey(0)

                if key == ord('b'):
                    cv2.imshow('frame',prev_frame)
                    key = cv2.waitKey(0)
        else:
            break

        if key==ord('q'):
            break;

    cap.release()

    cv2.destroyAllWindows()

play(video_file_path, fps, width, height, monochrome)


#get_ipython().system('(jupyter nbconvert --to script Video_playback.ipynb)')

