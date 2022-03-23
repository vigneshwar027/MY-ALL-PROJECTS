import cv2, time

photo = cv2.VideoCapture(0)
check,frame = photo.read()
cv2.imshow('Captured Photo',frame)
cv2.waitKey(0)

# this works without video.release()command and i dont know why it is used

