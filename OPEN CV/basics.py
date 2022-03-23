import cv2

img=cv2.imread('E:\DOWNLOADS\images (1).jpg',1)
# 1=color ; 0 = BnW ; -1 = fill color inside the object
resized_pic = cv2.resize(img,(int(img.shape[1]*2),int(img.shape[0]*2))) #to resize symmterically
# resized_pic = cv2.resize(img,(300,300)) #to resize freely

cv2.imshow('photo',resized_pic)
# cv2.imwrite('E:\DOWNLOADS\Vicky.jpg',resized_pic)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(img)
print(resized_pic)





