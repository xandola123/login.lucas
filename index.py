from tkinter import *
from tkinter import messagebox
from tkinter import ttk

#====Criar janela
jan = Tk()
jan.title("DP System - Acess Panel")
jan.geometry("1200x600")
jan.configure(background="white")
jan.resizable(width=False, height=False)

#======Adicionando imagens
imagem = PhotoImage(file="icons/imagem.png")

#======Widgets
LetFrame = Frame(jan, width=400, height=600, bg="GREEN", relief="raise")
LetFrame.pack(side=LEFT)

RightFrame = Frame(jan, width=790, height= 600, bg="GREEN", relief="raise")
RightFrame.pack(side=RIGHT)

LogoLabel = Label(LetFrame, image=imagem, bg="GREEN")
LogoLabel.place(x=100, y=200)

#=====Username
UserLabel = Label(RightFrame, text="Username:", font=("Arial", 20), bg="GREEN", fg="White")
UserLabel.place(x =150, y=290)

UserEntry = ttk.Entry(RightFrame, width=60)
UserEntry.place(x=300, y=300)

#======Password
PassLabel = Label(RightFrame, text="Password:", font=("Arial", 20), bg="GREEN", fg="White")
PassLabel.place(x =150, y=360)

PassEntry = ttk.Entry(RightFrame, width=60)
PassEntry.place(x=300, y=370)

jan.mainloop()