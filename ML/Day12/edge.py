import cv2 as cv
import numpy as np
img=cv.imread('walking.png',0)
edges=cv.Canny(img,100,200)
edges2=cv.Canny(img,0,220)
img1=np.hstack((img,edges,edges2))
cv.imshow('dst',img1)
cv.waitKey(0)
