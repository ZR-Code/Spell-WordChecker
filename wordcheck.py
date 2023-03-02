# Initilizaions
from tkinter import *
root = Tk()
root.geometry("800x300")
root.configure(background="White")
root.resizable(False, False)
pallete = ["FAF3DD", "17183B", "8FC0A9", "3F88C5", "F18805"]
text = Text(root, height=7, width=75, background="#FAF3DD", foreground="Black", insertbackground="Black", font="Roboto").place(x=55, y=50)



words = "input('What do you want to word check: ')"
split = words.split(" ")
spaceless = [x for x in split if x != '']
print(spaceless)
print(len(spaceless))
root.mainloop()
