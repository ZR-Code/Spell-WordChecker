# Initilizaions
from tkinter import *
root = Tk()
root.geometry("800x300")
root.configure(background="White")
root.resizable(False, False)
pallete = ["FAF3DD", "17183B", "8FC0A9", "3F88C5", "F18805"]

# Functions
def get_text():
    val = text.get(1.0, "end-1c")
    split = str(val).split(" ")
    spaceless = [x for x in split if x != '']
    print(len(spaceless))

# Visual Feautures
text = Text(root, background="#FAF3DD", foreground="Black", insertbackground="Black", font="Roboto", height=8, width=65)
get_words = Button(root, text="Get Words", command=get_text).place(x=100, y=25)

text.pack()

words = "input('What do you want to word check: ')"

root.mainloop()