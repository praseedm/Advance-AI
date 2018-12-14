#!/usr/bin/python
from Tkinter import *
def myhan():
 b_l[0].grid_remove()
mwin=Tk()
a=StringVar()
sv_l=list()
b_l=list()
but1=Button(mwin,text='Remove',command=myhan)
for i in range(10):
 sv_l.append(StringVar())
for i in range(5): 
 for j in range(2):
  b_l.append(Entry(mwin,width=10,textvariable=sv_l[2*i+j]))
for i in range(5): 
 for j in range(2):
  b_l[2*i+j].grid(row=i, column=j)
for i in range(5): 
 for j in range(2):
  sv_l[2*i+j].set('i=%d j=%d'%(i,j))
but1.grid(row=6,column=0)
mwin.mainloop()
