import cv2 as cv
import numpy as np
src = cv.VideoCapture(0)

while 1 :
    check,frame = src.read()
    cv.imshow('Actual video',frame)

    hsv_img = cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    lower_limit = np.array([110,50,50])
    upper_limit = np.array([130,252,252])
    # the above is blue color
    
    captured = cv.inRange(hsv_img,lower_limit,upper_limit)
    cv.imshow("Captured",captured)
    res_img=cv.bitwise_and(frame,frame,mask=captured)
    cv.imshow("Residue Image",res_img)
    if cv.waitKey(1) == ord('b'):
        break
