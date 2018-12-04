import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
img=cv.imread('apple.jpg',0)
plt.hist(img.ravel())
plt.show()
