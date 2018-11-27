import cv2 as cv
import numpy as np
img=np.zeros((512,512,3),np.uint8)
cv.line(img,(0,0),(511,511),(255,255,255),10)
cv.rectangle(img,(384,0),(510,128),(255,0,0),3)

cv.imshow('d1',img)
cv.waitKey(0)

