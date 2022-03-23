import cv2 as cv
import numpy as np
img = cv.imread('vicky.png',0)
kernel = np.ones((5,5),np.float32)/25
blurred_img = cv.filter2D(img,-1,kernel)
cv.imshow('Actimage',img)
cv.imshow('BLurred image',blurred_img)

# or instead of creating kernel on our own 
# simply define the method the action like blur,edge detect,gausian blur etc
# and simply just define the matrix size in it
# below example

blur2 = cv.blur(img,(5,5),0)
cv.imshow('Blur',blur2)

gaussian_blur = cv.GaussianBlur(img,(5,5),0)
cv.imshow('Gaussian_Blur',gaussian_blur)
cv.waitKey()
