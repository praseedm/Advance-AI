#!/usr/bin/env python2



def init():
	global mymod
	import mymod

def show():
	print(mymod.a+mymod.b)

def re():
	global mymod
	reload(mymod)

i=4

while(i != 0):
	i=input( "Enter \n\t0-Exit\n\t1-Initialize\n\t2-show\n\t3-reload\n")
	if(i == 1):
		init()
	elif(i == 2):
		show()
	elif(i == 3):
		re()

print("exiting..")


	 

