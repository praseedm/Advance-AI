import numpy as np
import cv2 as cv
face_cascade=cv.CascadeClassifier('haarcascade_face.xml')
eye_cascade=cv.CascadeClassifier('haarcascade_eye.xml')
img=cv.imread('faces.jpg')
gray=cv.cvtColor(img,cv.COLOR_BGR2GRAY)
faces=face_cascade.detectMultiScale(gray,1.1)
for (x,y,w,h) in faces:
	cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
	roi_gray=gray[y:y+h,x:x+w]
	roi_color=img[y:y+h,x:x+w]
	eyes=eye_cascade.detectMultiScale(roi_gray)
	
	for (ex,ey,ew,eh) in eyes:
		cv.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)




cv.imshow('dst',img)
cv.waitKey(0)
