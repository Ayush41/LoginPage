#importing some modules:-->
from tkinter import *
from PIL import Image, ImageTk

root = Tk()
root.geometry("500x400+450+100")
root.title("login page")

bg = Image.open("anime.jpg")#__image to be enter__>
bg = bg.resize((500,500))
bg1 = ImageTk.PhotoImage(bg)
Label(root, image=bg1).grid(row=0,column=0)

Label(root,text="PYTHUSH's login page",font="algerian 25").place(x=120,y=90)
Label(root,text="EMAIL OR PHONE :",font="comicsansma 15",bg="grey").place(x=50,y=150)
Entry(root,font="comicsansma 15").place(x=250,y=150)

Label(root,text="PASSWORD :", font="comicsansma 15",bg="grey").place(x=50,y=200)
Entry(root,font="comicsansma 15").place(x=250,y=200)

#THIS IS FOR BUTTON TO-->"SUBMIT"
Button(root,text="submit",font="arial 15",fg="white",bg="#006080").place(x=200,y=300)
root.mainloop()