import cv2 as cv
import numpy as np
img=cv.imread('opencvlogo.png')
blur=cv.blur(img,(5,5))
cv.imwrite('blur.jpg',blur)
cv.imshow('dst',blur)
cv.waitKey(0)



