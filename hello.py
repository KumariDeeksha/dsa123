import tkinter as tk
from tkinter import *
from tkinter import messagebox
import os,time,winsound

def createWidgets():

  labell=Label(root,text="Enter the time in hh:mm-")
  labell.grid(row=0,column=0,padx=5,pady=5)


  global entry1
  entry1=Entry(root,width=15)
  entry1.grid(row=0,column=1)

  label2=Label(root,text="Enter the message of alarm-")
  label2.grid(row=0,column=0,padx=5,pady=5)

  global entry2
  entry2=Entry(root,width=15)
  entry2.grid(row=0,column=1)



root =tk.Tk()
root.title("Alarm clock")
root.geometry("400*150")

root.mainloop()
