# Initilizaions
from tkinter import *
root = Tk()
root.geometry("800x300")
root.configure(background="White")
root.resizable(False, False)
words = input('What do you want to word check: ')
split = words.split(" ")
spaceless = [x for x in split if x != '']
print(spaceless)
print(len(spaceless))
root.mainloop()
