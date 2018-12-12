#!/usr/bin/env python
import matplotlib.pyplot as plt
fobj=plt.figure(figsize=(4,4),facecolor='#00FF00')
spobj1=fobj.add_subplot(221,axisbg='#0000FF')
spobj1=fobj.add_subplot(222,polar=True)
spobj1=fobj.add_subplot(223)
plt.show()
