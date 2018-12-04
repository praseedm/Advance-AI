import cv2
import numpy as np

img = cv2.imread('new.jpg',0)
kernel = np.ones((4,4),np.uint8)
r = cv2.erode(img,kernel,iterations = 1)
r = cv2.dilate(img,kernel,iterations = 1)
#img=np.hstack((img,erosion))



cv2.imshow('dst',r)
cv2.waitKey(0)
