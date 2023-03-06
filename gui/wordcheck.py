# Initilizaions
from tkinter import *
from tkinter import ttk
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
root.resizable(True, False)
pallete = ["FAF3DD", "17183B", "8FC0A9", "3F88C5", "F18805"]


# Visual Feautures

text = Text(root, background="White", foreground="Black", insertbackground="Black", font="Roboto", height=50, width=45)
# Functions
def clear_text():

    try:
        text.delete("1.0", "end")
        lblfrmeanswer.destroy()
    except NameError:
        text.delete("1.0", "end")
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
    print('The Corrected sentence is: ' + ''.join(fixed))

    # Scrollbar
    global lblfrmeanswer
    lblfrmeanswer = Frame(root, background='White')
    lblfrmeanswer.pack(pady=35, fill=BOTH, expand=1)
    mycanvas = Canvas(lblfrmeanswer)
    mycanvas.pack(side=LEFT, fill=BOTH, expand=1)
    scroll = ttk.Scrollbar(lblfrmeanswer, orient=VERTICAL, command=mycanvas.yview)
    scroll.pack(side=RIGHT, fill=Y)
    mycanvas.configure(yscrollcommand=scroll.set)
    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox("all")))
    sec_frame = Frame(mycanvas, background='White')
    mycanvas.create_window((0,0), window=sec_frame, anchor="nw")
    correct_msg = Message(sec_frame, text="The corrected sentence is: " + ''.join(fixed), background='White').pack()
    words_msg = Label(sec_frame, text="The amount of words in your text is: " + str(len(spaceless)) + '\n' + '\n', background='White').pack()
    # Visuals
    og = Label(text="Original Text", font=("Calibri", 18), background="#FAF3DD").place(x=145, y=7)
    after = Label(text="Corrected Text and Word Amount", font=("Calibri", 18), background="#FAF3DD").place(x=500, y=7)


 
    print("The amount of words in the text is: " + str(len(spaceless)))
# More Visuals
get_words = customtkinter.CTkButton(master=root, text="Get Words", command=get_text, fg_color=('#8FC0A9'), text_color = ('Black'), border_width=1, hover_color='#F18805', border_color='Black', corner_radius=20).place(x=350, y=268)
clear = customtkinter.CTkButton(master=root, text = "Clear Text", command=clear_text, fg_color=("#3F88C5"), text_color=("Black"), corner_radius=20, border_width=1, hover_color="#e1f222").place(x=350, y =5)

text.pack(padx=5, pady=35, side=LEFT)

root.mainloop()
