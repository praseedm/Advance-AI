#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(6,6),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
yn=np.random.randint(1,100,10)
xn=np.arange(2,21,2)
yn.sort()
print type(spobj)
spobj.plot(xn,yn,'ro:',drawstyle='steps-mid')
print 'xn=',xn
print 'yn=',yn
plt.show()
