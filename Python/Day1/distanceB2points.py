#!/bin/usr/env python


### fruitful function to return distance between 2 points in XY plane ###

import math

def distance(x1,y1,x2,y2):
	distance = math.sqrt( (x1-x2)**2 + (y1-y2)**2 )
	return distance

x1=input("Enter x1 : ")
y1=input("Enter y1 : ")
x2=input("Enter x2 : ")
y2=input("Enter y2 : ")

print "Distance between points : ", distance(x1,y1,x2,y2)
