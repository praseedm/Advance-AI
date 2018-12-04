import cv2
import numpy as np

A = cv2.imread('apple.jpg')
G = A.copy()

for i in range(4):
    G = cv2.pyrDown(G)
    cv2.imshow('d1',G)
    cv2.waitKey(0)



