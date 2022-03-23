import cv2 as cv
img = cv.imread('vicky.png',0) #the src should be a grayscale img
ret,thres = cv.threshold(img,70,255,cv.THRESH_BINARY)
# in the above the 1st arg is src ,thres limit, pixel value setpoint for those that exceeded the threshold limit

cv.imshow("thresholded image",thres)
cv.waitKey(0)
