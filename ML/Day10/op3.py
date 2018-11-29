import cv2 as cv
import numpy as np
img=cv.imread('messi.jpg')
blue=img[:,:,2]
#img[:,:,2]=255
#print(blue)
ball=img[280:340,330:390]
img[273:333,100:160]=ball
print(img.shape)
img.itemset((10,10,2),100)

cv.imshow('dt',img)
cv.waitKey(0)

