#!/usr/bin/env python
import sys
fd = open(sys.argv[1],'w')
for item in [x*int(sys.argv[2]) for x in range(10)]:
    i = 1
    fd.write(str(i)+" x "+sys.argv[2]+" = "+str(item)+"\n")
    i+=1
fd.close() 
