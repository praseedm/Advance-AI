#!/usr/bin/env python

### Write scipts for Problems 1 and 2.(using function with parameters) ###

def largest(num1,num2,num3):
	result = num1
	if(num2 > result):
		result = num2
	if(num3 > result):
		result = num3
	print "Largest : ",result

x=input("Enter 1st number : ")
y=input("Enter 2nd number : ")
z=input("Enter 3rd number : ")

largest(x,y,z)
