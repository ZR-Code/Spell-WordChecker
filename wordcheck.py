# Initilizaions
from tkinter import *
import customtkinter
from gingerit.gingerit import GingerIt
import pysbd, re

root = Tk()
parser = GingerIt()
segmentor = pysbd.Segmenter(language="en", clean=False)
subsegment_re = r'[^;:\n•]+[;,:\n•]?\s*'
root.title("Spell and Word Checker")
root.geometry("800x300")
root.configure(background="#FAF3DD")
root.resizable(False, False)
pallete = ["FAF3DD", "17183B", "8FC0A9", "3F88C5", "F18805"]

# Functions
def get_text():
    fixed = []
    val = text.get(1.0, "end-1c")
    split = str(val).split(" ")
    spaceless = [x for x in split if x != '']


    for space in segmentor.segment(val):
        if len(space) < 300:
            fixed.append(GingerIt().parse(space)['result'])

        else:
            subsegments = re.findall(subsegment_re, space)
            if len(subsegments) == 1 or any(len(v) < 300 for v in subsegments):
                print(f'Skipped: {space}') 
                fixed.append(space)
            else:
                res = []
                for s in subsegments:
                    res.append(GingerIt().parse(s)['result'])
                fixed.append("".join(res))
    print(''.join(fixed))
    print(len(spaceless))

# Visual Feautures
scrollbar_tk = Scrollbar(root)
scrollbar_tk.pack(side=RIGHT, fill=Y)
text = Text(root, background="White", foreground="Black", insertbackground="Black", font="Roboto", height=8, width=65, yscrollcommand=scrollbar_tk.set)
get_words = customtkinter.CTkButton(master=root, text="Get Words", command=get_text, fg_color=('#8FC0A9'), text_color = ('Black'), border_width=1, hover_color='#F18805', border_color='Black', corner_radius=20).place(x=345, y=200)

text.pack(padx=5, pady=50)
scrollbar_tk.config(command=text.yview)

root.mainloop()
