#!/usr/bin/env python
import sys
fd = open(sys.argv[1],'w')
i = 0
for item in [x*int(sys.argv[2]) for x in range(10)]:
    fd.write("%d x %s = %d\n"%(i,sys.argv[2],item))
    i+=1
fd.close() 
