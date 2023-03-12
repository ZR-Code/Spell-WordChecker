from tkinter import *
import customtkinter
master = Tk()
master.geometry("600x300")
master.resizable(False, False)

bg = PhotoImage(file='/Users/zaidr/Desktop/Coding/Word-Amount/pexels-resize-gradient.png')
bg_label = Label(master, image=bg)
bg_label.place(x=0,y=0)

tutorial = customtkinter.CTkButton(master=master, text="Tutorial", fg_color=("Light blue"))
master.mainloop()