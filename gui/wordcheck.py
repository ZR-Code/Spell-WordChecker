# Initilizaions
from tkinter import *
from tkinter import ttk
from gingerit.gingerit import GingerIt
import pysbd, re
from PIL import Image, ImageTk
import enterscreen
window = Tk()
news = enterscreen.Newscreen(window)


root = Tk()
parser = GingerIt()
segmentor = pysbd.Segmenter(language="en", clean=False)
subsegment_re = r'[^;:\n•]+[;,:\n•]?\s*'
root.title("Spell and Word Checker")
root.geometry("800x300")
root.configure(background="#FAF3DD")
root.resizable(False, False)
pallete = ["FAF3DD", "17183B", "8FC0A9", "3F88C5", "F18805"]
labelframeinput = LabelFrame(text="Your original text", background="#FAF3DD", foreground="Black")


# Visual Feautures
expand = Image.open("/Users/zaidr/Desktop/Coding/Word-Amount/gui/expand.png")
expand_size = expand.resize((25, 25))
expand_actual = ImageTk.PhotoImage(expand_size)
# Functions
def clear_text():

    try:
        text.delete("1.0", "end")
        lblfrmeanswer.destroy()
    except NameError:
        text.delete("1.0", "end")
def get_text():
    global fixed
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
    lblfrmeanswer = LabelFrame(root, text="Corrections and Amount of words", background='#FAF3DD', foreground="Black")
    lblfrmeanswer.pack(pady=35, fill=BOTH, expand=1)
    mycanvas = Canvas(lblfrmeanswer, background="White")
    mycanvas.pack(side=LEFT, fill=BOTH, expand=1)
    scroll = ttk.Scrollbar(lblfrmeanswer, orient=VERTICAL, command=mycanvas.yview)
    scroll.pack(side=RIGHT, fill=Y)
    mycanvas.configure(yscrollcommand=scroll.set)
    mycanvas.bind('<Configure>', lambda e: mycanvas.configure(scrollregion=mycanvas.bbox("all")))
    sec_frame = Frame(mycanvas, background='White')
    mycanvas.create_window((0,0), window=sec_frame, anchor="nw")
    correct_msg = Message(sec_frame, text="The corrected sentence is: " + ''.join(fixed), background='White', foreground="Black").pack()
    words_msg = Label(sec_frame, text="The amount of words in your text is: " + str(len(spaceless)) + '\n' + '\n', background='White', foreground="Black").pack()



 
    print("The amount of words in the text is: " + str(len(spaceless)))

class Scroll:
    def __init__(self, scrollableObject, text_for_msg):
        self.scrollableObject = scrollableObject
        self.text_for_msg = text_for_msg
    def y_expand(self, scrollableObject, text_for_msg):
        scrollableObject.pack(pady=35, fill=BOTH, expand=1)
        newcanvas = Canvas(scrollableObject, background="White")
        newcanvas.pack(side=RIGHT, fill=BOTH, expand=1)
        scrolling = ttk.Scrollbar(scrollableObject, orient=VERTICAL, command=newcanvas.yview)
        scrolling.pack(side=RIGHT, fill=Y)
        newcanvas.configure(yscrollcommand=scrolling.set)
        newcanvas.bind('<Configure>', lambda e: newcanvas.configure(scrollregion=newcanvas.bbox("all")))
        new_frame = Frame(newcanvas, background="#FAF3DD")
        newcanvas.create_window((0,0), window=new_frame, anchor="nw")
        Message(new_frame, text=text_for_msg, font="Roboto", background="#FAF3DD", foreground="Black").pack(side=LEFT)


class Expand():
    def expand_in(self):

        new = Toplevel(root)
        new.geometry("800x550")
        new.configure(background="#FAF3DD") 
        new.resizable(False, False)
        labelmes = LabelFrame(new, background="#FAF3DD")
        uniscroll = Scroll(labelmes, text.get(1.0, "end-1c"))
        Scroll.y_expand(self, labelmes, text.get(1.0, "end-1c"))
    def expand_out(self):
        new_out = Toplevel(root)
        new_out.geometry("800x550")
        new_out.configure(background="#FAF3DD")
        new_out.resizable(False, False)
        labelout = LabelFrame(new_out, background="#FAF3DD")
        try:
            outscroll = Scroll(labelout, ''.join(fixed))
            Scroll.y_expand(self, labelout, ''.join(fixed))
        except NameError:
            print("Press Submit before you press this button")


expand_area = Expand()



# More Visuals
get_words = ttk.Button(master=root, text="Get Words", style="Custom.TButton", command=get_text).place(x=350, y=268)
clear = ttk.Button(master=root, text = "Clear Text", style="C.TButton", command=clear_text).place(x=350, y =5)
style = ttk.Style()
style.theme_use('default')
style.configure("Custom.TButton", background="#8FC0A9", borderwidth='1', focuscolor='none', borderradius=15)
style.configure("C.TButton", background="#3F88C5", borderwidth='1', focuscolor="none", borderradius=15)

text = Text(labelframeinput, background="White", foreground="Black", insertbackground="Black", font="Roboto", height=50, width=45)
expand_right = Button(root, text="expand", image=expand_actual, compound=LEFT, background="#FAF3DD", command=expand_area.expand_out).place(x=650, y=268)
expand_left = Button(root, text="expand", image=expand_actual, compound=LEFT, command= expand_area.expand_in).place(x=50, y=268)


labelframeinput.pack(padx=5, pady=35, side=LEFT)
text.pack(padx=2, pady=10, side=LEFT)

root.mainloop()
