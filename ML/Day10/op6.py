import numpy as np
import cv2 as cv
img=cv.imread('ml.png',0)
rows,cols=img.shape
M=cv.getRotationMatrix2D(((cols-1)/2,(rows-1)/2),90,1)
dst=cv.warpAffine(img,M,(cols,rows))
cv.imshow('dt',dst)
cv.waitKey(0)
