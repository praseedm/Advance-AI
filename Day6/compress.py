#!/usr/bin/env python
import sys
open(sys.argv[1],'w').write( "\n".join( ["%d x %s = %d"%(x,sys.argv[2],x*int(sys.argv[2])) for x in range(11)] ))
