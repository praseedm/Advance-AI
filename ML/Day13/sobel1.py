import cv2 as cv
import numpy as np
img=cv.imread('sudoku.png',0)
sobelx=cv.Sobel(img,cv.CV_64F,1,0,ksize=1)
sobely=cv.Sobel(img,cv.CV_64F,0,1,ksize=1)
cv.imshow('dst',sobely)
cv.waitKey(0)

