import pyshorteners
from tkinter import *

def short():
    url = e1.get()
    s = pyshorteners.Shortener().tinyurl.short(url)
    
    e2.insert(END,s)
    
root=Tk()
root.geometry("500x400")
root.title("URL Shortener")

l1=Label(root,text="URL SHORTENER",font="Cambria 30 bold",fg="blue")
l1.pack(pady=10)

l2=Label(root,text="Enter URL",font="Cambria 20 bold",fg="green")
l2.pack(pady=10)

e1 = Entry(root,font="Cambria 15",bd=3,width=40)
e1.pack()

b=Button(root,text="Click here",font="Cambria 20 bold",fg="red",command=short)
b.pack(pady=10)

l2=Label(root,text="New URL",font="Cambria 20 bold",fg="green")
l2.pack(pady=10)

e2=Entry(root,font="Cambria 15",width=25)
e2.pack()

mainloop()