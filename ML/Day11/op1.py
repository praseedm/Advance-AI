import cv2 as cv
import numpy as np

img=cv.imread('sudoku.jpg',0)

ret=cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,cv.THRESH_BINARY,11,2)
print(ret)
cv.imwrite('1.jpg',ret)

cv.imshow('dst',ret)
#cv.imshow('dst',img)
cv.waitKey(0)
