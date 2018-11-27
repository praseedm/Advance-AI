import numpy as np
import cv2 as cv
img=np.zeros((512,512,3),np.uint8)
img[1:100,1:100]=(255,255,0)
print(img)
cv.imshow('d1',img)
cv.waitKey(0)

