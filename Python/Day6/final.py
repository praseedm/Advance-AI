#!/usr/bin/env python
import sys
fd = open(sys.argv[1],'w')
i = 0
for item in [x*int(sys.argv[2]) for x in range(10)]:
    fd.write(str(i)+" x "+sys.argv[2]+" = "+str(item)+"\n")
    i+=1
fd.close()
