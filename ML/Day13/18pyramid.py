import cv2
img = cv2.imread('messi5.jpg')
lower = cv2.pyrDown(img)
print(lower.shape)
cv2.imshow('dst',img)
cv2.destroyAllWindows()
