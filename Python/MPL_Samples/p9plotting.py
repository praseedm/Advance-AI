#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
fobj=plt.figure(figsize=(4,4),facecolor='#00FF00')
spobj=fobj.add_subplot(1,1,1)
an=np.random.randint(1,100,10)
spobj.plot(an)
print an
plt.show()
