#!/usr/bin/python
from Tkinter import *
mwin=Tk()
vexp=''
def b1han():
 global vexp
 vexp+='1'
 t1.set(vexp)
def b2han():
 global vexp
 vexp+='2'
 t1.set(vexp)
def bphan():
 global vexp
 vexp+='+'
 t1.set(vexp)
def behan():
 global vexp
 t1.set(str(eval(vexp)))
 vexp=''

mwin.title('calc')
t1=StringVar()
e1=Entry(mwin,textvariable=t1)
b1=Button(mwin,text='1',command=b1han)
b2=Button(mwin,text='2',command=b2han)
b3=Button(mwin,text='3')
b4=Button(mwin,text='4')
bp=Button(mwin,text='+',command=bphan)
bm=Button(mwin,text='-')
be=Button(mwin,text='=',command=behan)
e1.grid(row=0,column=0,columnspan=4)
b1.grid(row=1,column=0)
b2.grid(row=1,column=1)
b3.grid(row=2,column=0)
b4.grid(row=2,column=1)
bp.grid(row=1,column=2)
bm.grid(row=1,column=3)
be.grid(row=2,column=2,columnspan=2)

mwin.mainloop()
