from tkinter import *
from tkinter import ttk,messagebox

GUI = Tk()
GUI.title('Hello World')
GUI.geometry('500x500')

L1 = Label(GUI,text='Hello World', font=(None,20))
L1.pack()

B1 = Button(GUI,text='Click me!',command=popup)
B1.pack()

L = Label(GUI,text="your username")
L.pack()


GUI.mainloop()