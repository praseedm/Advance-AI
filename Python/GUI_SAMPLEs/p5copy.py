#!/usr/bin/python
from Tkinter import *
def bhan():
 t2.set(t1.get())
mwin=Tk()
mwin.title('SW200')
t1=StringVar()
t2=StringVar()
e1=Entry(mwin,width=30,textvariable=t1)
e2=Entry(mwin,width=30,textvariable=t2)
t1.set('sample')
b1=Button(mwin,text='click',command=bhan)
e1.pack()
b1.pack()
e2.pack()
mwin.mainloop()
