import cv2 as cv

img = cv.imread('vicky.png',1)
cv.imshow('Photo',img)
def mouse_action(event,x,y,flags,param):      

    if event == cv.EVENT_LBUTTONDOWN:
        font=cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img,'left clicked',(x,y),font,1,(255,0,0),2)
        cv.imshow('Photo',img)

    if event == cv.EVENT_RBUTTONDOWN:
        font=cv.FONT_HERSHEY_SIMPLEX
        cv.putText(img,'Right clicked',(x,y),font,1,(255,0,0),2)
        cv.imshow('Photo',img)
    # if event == cv.EVENT_RBUTTONDBLCLK:
    #     font=cv.FONT_HERSHEY_SIMPLEX
    #   cv.circle(img,(x,y),200,5)  

# to define window size

cv.namedWindow('Photo',cv.WINDOW_FULLSCREEN)
cv.setMouseCallback('Photo',mouse_action)


cv.waitKey(0)
