# Initilizaions
from tkinter import *
from spellchecker import SpellChecker
root = Tk()
root.geometry("800x300")
root.configure(background="#FAF3DD")
root.resizable(False, False)
proper_spelling = SpellChecker()
pallete = ["FAF3DD", "17183B", "8FC0A9", "3F88C5", "F18805"]

# Functions
def get_text():
    val = text.get(1.0, "end-1c")
    split = str(val).split(" ")
    spaceless = [x for x in split if x != '']
    maybe_missed = proper_spelling.unknown(spaceless)
    
    for word in maybe_missed:
        print(proper_spelling.correction(word))

    print(len(spaceless))

# Visual Feautures
scrollbar_tk = Scrollbar(root)
scrollbar_tk.pack(side=RIGHT, fill=Y)
text = Text(root, background="White", foreground="Black", insertbackground="Black", font="Roboto", height=8, width=65, yscrollcommand=scrollbar_tk.set)
get_words = Button(root, text="Get Words", command=get_text, bg='#17183B').place(x=345, y=200)

text.pack(padx=5, pady=50)
scrollbar_tk.config(command=text.yview)


words = "input('What do you want to word check: ')"

root.mainloop()
