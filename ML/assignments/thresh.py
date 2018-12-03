#!/usr/bin/env python

import numpy as np
import cv2 as cv

img = cv.imread('gradient.jpg',0)
thresholds = [cv.THRESH_BINARY,cv.THRESH_BINARY_INV,cv.THRESH_TRUNC,cv.THRESH_TOZERO,cv.THRESH_TOZERO_INV]
new = img 

for thresh in thresholds:
    ret,dt = cv.threshold(img,127,255,thresh) 
    new = np.hstack((new,dt))

cv.imshow('dt',new)    
cv.waitKey(0)