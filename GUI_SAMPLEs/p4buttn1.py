#!/usr/bin/python
from Tkinter import *
mwin=Tk()
a=StringVar()
for i in range(5): 
 for j in range(2):
  s=StringVar()
  b=Entry(mwin,width=10,textvariable=s)
  s.set('i=%d j=%d'%(i,j))
  b.grid(row=i, column=j)
mwin.mainloop()
