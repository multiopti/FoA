# -*- coding: utf-8 -*-
"""
Created on Thu Jan 20 14:50:53 2022

@author: Admin
"""

# Import Required Module
from tkinter import *
from tkinter.ttk import *
 
# Create Object
root = Tk()
 
# Set geometry (widthxheight)
root.geometry('300x200')
 
# This will create style object
style = Style()
 
# This will be adding style, and
# naming that style variable as
# W.Tbutton (TButton is used for ttk.Button).
style.configure('W.TButton', font =
               ('calibri', 10, 'bold', 'underline'),
                foreground = 'red')
 
# Style will be reflected only on
# this button because we are providing
# style only on this Button.
''' Button 1'''
btn1 = Button(root, text = 'Quit !',
                style = 'W.TButton',
             command = root.destroy)
btn1.grid(row = 1, column = 3, padx = 100)
 
''' Button 2'''
 
btn2 = Button(root, text = 'Click me !', command = None)
btn2.grid(row = 0, column = 3, pady = 10, padx = 100)
 
# Execute Tkinter
root.mainloop()