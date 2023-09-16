#importing some modules:-->
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x400+450+100")
root.title("login page")

#THIS IS FOR BUTTON TO-->"SUBMIT"
Button(root,text="submit",font="arial 15",fg="white",bg="#006080").place(x=200,y=300)
root.mainloop()