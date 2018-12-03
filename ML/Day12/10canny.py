import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('face.jpg',0)
edges = cv2.Canny(img,0,200)
edges2 = cv2.Canny(img,100,200)

pic=np.hstack((img,edges,edges2))

'''
plt.subplot(121),plt.imshow(img,cmap = 'gray')
plt.title('Original Image'), plt.xticks([]), plt.yticks([])
plt.subplot(122),plt.imshow(edges,cmap = 'gray')
plt.title('Edge Image'), plt.xticks([]), plt.yticks([])

plt.show()i
'''

cv2.imshow('dst',pic)
cv2.waitKey(0)
