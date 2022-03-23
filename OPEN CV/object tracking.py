import cv2 as cv
# import numpy as np

org = cv.imread('colors.png',1)
cv.imshow('Original',org)

hsv_img = cv.cvtColor(org,cv.COLOR_BGR2HSV)
# lower_limit = np.array([36, 25, 25])
# upper_limit = np.array([70, 255,255])

mask = cv.inRange(hsv_img,(36, 25, 25),(70, 255,255))
cv.imshow("Masked",mask)
res_img=cv.bitwise_and(org,org,mask=mask)
cv.imshow("Residue Image",res_img)
cv.waitKey(0)
