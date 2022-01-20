# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 14:46:07 2022

@author: Admin
"""

#Import tkinter library
from tkinter import *
#Create an instance of Tkinter frame or window
win= Tk()
#Set the geometry of tkinter frame
win.geometry("750x250")
def callback():
   Label(win, text="Hello World!", font=('Century 20 bold')).pack(pady=4)
#Create a Label and a Button widget
btn=Button(win, text="Press Enter", command= callback)
btn.pack(ipadx=10)
win.bind('<Return>',lambda event:callback())
win.mainloop()