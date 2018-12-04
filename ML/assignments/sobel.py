#!/usr/bin/env python

import  cv2 as cv


b_img = cv.imread('building.png',0)

sobelx = cv.Sobel(b_img,cv.CV_16U,1,0,ksize=1)
cv.imwrite('buil_sobx16.jpg',sobelx)

sobelx = cv.Sobel(b_img,cv.CV_32F,1,0,ksize=1)
cv.imwrite('buil_sobx32.jpg',sobelx)

sobelx = cv.Sobel(b_img,cv.CV_64F,1,0,ksize=1)
cv.imwrite('buil_sobx64.jpg',sobelx)