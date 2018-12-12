#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(10,10),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
yn=np.random.randint(1,100,9)
xn=np.arange(2,20,2)
xts=np.linspace(0,20,5)
yn.sort()
spobj.plot(xn,yn,'ro:',drawstyle='steps',label='Single')
spobj.plot(xn,yn*2,'bo:',drawstyle='steps',label='Double')
spobj.set_xticks(xts)
spobj.set_xticklabels(['zero','Quartile1','Half','Quartile3','Full'],rotation=30,fontsize='small')
spobj.set_xlabel('Parts')
spobj.set_title('A sample plot')
spobj.legend(loc='best')
print 'xn=',xn
print 'yn=',yn
plt.show()
