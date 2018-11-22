#!/usr/bin/python
from Tkinter import *
def myhan(e):
 print 'clicked at %d-%d'%(e.x,e.y)
mwin=Tk()
mwin.title('SW200')
mwin.geometry('200x200')
lb1=Label(mwin)
lb1.config(text='This is a sample label',bg='green')
lb1.bind('<Button-1>',myhan)
#lb1.pack(side=LEFT,fill=BOTH,expand=1)
lb1.place(x=10,y=10,height=50)
mwin.mainloop()
