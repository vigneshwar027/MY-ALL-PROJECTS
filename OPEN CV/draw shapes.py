import cv2 as cv

photo = cv.imread('E:\DOWNLOADS\images (1).jpg',1)
cv.line(photo,(0,0),(200,200),(255,0,0),4)
cv.rectangle(photo,(10,10),(300,300),(0,255,0),3)
cv.circle(photo,(300,300),100,(0,255,0),-1)
font = cv.FONT_HERSHEY_TRIPLEX
cv.putText(photo,'hi vicky',(40,400),font,2,(0,255,255))
cv.imshow('Photo with drawings',photo)
cv.waitKey(0) 
cv.destroyAllWindows()