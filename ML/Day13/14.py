import cv2
import numpy as np

img = cv2.imread('j2.png',0)
kernel = np.ones((5,5),np.uint8)
closing = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
img=np.hstack((img,closing))
cv2.imshow('dst',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
