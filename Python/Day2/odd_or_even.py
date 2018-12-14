#!/usr/bin/env python

### Write scipts for Problems 1 and 2.(using function with parameters) ###

def oddoreven(number):
	if(number % 2 == 0):
		print number, " is even"
	else:
		print number, " is odd"

x=input("Enter number : ")
oddoreven(x)
