import numpy as np
import cv2 as cv
img=cv.imread('messi.jpg',0)
rows,cols=img.shape
M=np.float32([[1,0,100],[0,1,50]])
dst=cv.warpAffine(img,M,(cols,rows))
cv.imshow('dt',dst)
cv.waitKey(0)
