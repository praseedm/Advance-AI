#!/usr/bin/env python

import sys
import os
import matplotlib.pyplot as plt

if len(sys.argv) < 2:
	print "Error!! argument missing"
	exit()

dir_name = sys.argv[1]

if os.path.isdir("./"+dir_name) == False:
	print "Error!! no directory Exists"
	exit()	

if len(os.listdir('./'+dir_name) ) == 0:
 	print "Error!!Directory is empty"
	exit()

os.system('ls -l ./'+dir_name+' > ./test.txt')

lines = open('test.txt').readlines()

sizes = []
filenames = []

for i in lines[1:]:
	l = i.split()
	sizes.append(int(l[4]))
	filenames.append(l[8])

fobj=plt.figure()
spobj=fobj.add_subplot(1,1,1)
spobj.set_title('Filesize plot',fontsize=18)
spobj.set_xlabel('Filename')
spobj.set_ylabel('Filesizes')
spobj.bar(range(len(sizes)),sizes)
spobj.set_xticklabels([1]+filenames,rotation=10)
plt.show()