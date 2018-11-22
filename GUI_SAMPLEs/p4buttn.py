#!/usr/bin/python
from Tkinter import *
def bhan():
 print 'Button clicked',
mwin=Tk()
b1=Button(mwin,text='click',command=bhan)
b1.pack()
mwin.mainloop()
