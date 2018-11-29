import cv2 as cv
import numpy as np
img=cv.imread('messi.jpg')
px=img[100,100]
print (px)

blue= img[100,100,2]
img[100:110,100:110]=[255,255,255]

img[273:333,100:160]=img[280:340,330:390]
img[:,:,0]=0
cv.imshow('d',img)
cv.waitKey(0)

