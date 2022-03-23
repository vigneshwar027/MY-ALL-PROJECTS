import cv2
a=1
while True:
    a+=1
    video = cv2.VideoCapture(0)
    check,frame = video.read()
    # gray_img = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    # if required to conert to bnw
    cv2.imshow('Video capturing',frame)
    
    if cv2.waitKey(1) == ord('b'):
        break
print('Total number of frames: ', a)


# this works without video.release()command and i dont know why it is used


