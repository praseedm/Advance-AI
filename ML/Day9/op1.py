import cv2 as cv

img=cv.imread('walking.jpg',0)
print(img.shape)
print(img)
cv.imshow('image',img)
k=cv.waitKey(0)

