#!/usr/bin/python
from Tkinter import *
mwin=Tk()
mwin.title('SW200')
lb1=Label(mwin)
lb1.config(height=10,width=20,text='This is a sample label')
lb1.config(bg='#00F',fg='red')
fnt=('Times',20,'bold')
lb1.configure(font=fnt)
lb1.pack()
mwin.mainloop()
