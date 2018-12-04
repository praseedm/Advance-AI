import  cv2
import numpy as np
from matplotlib import pyplot as plt
img = cv2.imread('sudoku.png',0)
#laplacian = cv2.Laplacian(img,cv2.CV_64F)
sobelx = cv2.Sobel(img,cv2.CV_8U,1,0,ksize=1)
sobely = cv2.Sobel(img,cv2.CV_8U,0,1,ksize=1)
cv2.imshow('dst',sobelx)
cv2.waitKey(0)
