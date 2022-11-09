from __future__ import print_function
import cv2 as cv
import argparse
import numpy as np
max_value = 255
max_value_H = 255
gray_l=0
gray_h= max_value_H
window_capture_name = 'Video Capture'
window_detection_name = 'Object Detection'
Threshold_name = 'BAR'

def thresh_trackbar(val):
    global gray_l
    global gray_h
    gray_l = val
    gray_l = min(gray_h-1, gray_l)
    cv.setTrackbarPos(Threshold_name, window_detection_name, gray_l)
    cv.setTrackbarPos()

parser = argparse.ArgumentParser(description='Code for Thresholding Operations using inRange tutorial.')
parser.add_argument('--camera', help='Camera divide number.', default=0, type=int)
args = parser.parse_args()
cap = cv.VideoCapture(0)
cv.namedWindow(window_capture_name)
cv.namedWindow(window_detection_name)
cv.createTrackbar(Threshold_name, window_detection_name , gray_l, max_value_H,  thresh_trackbar)
while True:
 
    ret, frame = cap.read()
    if frame is None:
        break
    frame_gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    frame_threshold = cv.inRange(frame_gray, (gray_l), (gray_h))
    cv.imshow(window_capture_name, frame)
    cv.imshow(window_detection_name,frame_threshold )
    
    key = cv.waitKey(30)
    if key == ord('q') or key == 27:
        break