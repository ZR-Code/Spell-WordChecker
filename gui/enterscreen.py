from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

root = Tk()

class Newscreen:
    def __init__(self, main):
        self.main = main
        main.title("Spell and Word Checker")
        main.resizable(False, False)
        main.geometry("600x300")
        main.configure(background="#DAF1F7")

        self.getstarted =Label(main, text="Get Started", font=("Comfortaa", 36), background="#DAF1F7")
        self.getstarted.place(x=185, y=10)

        self.tutorial = ttk.Button(master=main, text="Tutorial", style="Custom.TButton", command=self.tut)
        self.tutorial.place(x=100, y=120)

        self.jumpin = ttk.Button(master=main, text="Jump In", style="C.TButton", command=lambda: main.quit())
        self.jumpin.place(x=350, y=120)

        style = ttk.Style()
        style.theme_use('default')
        style.configure("Custom.TButton", background="#c2f970", foreground='Black', borderwidth='1', focuscolor='none', borderradius=15)
        style.configure("C.TButton", background="#fea82f", foreground="Black", borderwidth='1', focuscolor='none', borderradius=15)
        
    def tut(self):
        self.main.destroy()
        new = Tk()
        new.geometry("600x300")
        new.configure(background="#DAF1F7")
        new.title("Spell and Word Checker")
        new.resizable(False, False)

        startup = Image.open("/Users/zaidr/Desktop/Coding/Word-Amount/sartupmenu.png")
        startup_size = startup.resize((400,150))
        startup_actual = ImageTk.PhotoImage(startup_size)
        uparrows = Image.open("/Users/zaidr/Desktop/Coding/Word-Amount/arrows.png")
        uparrows_size  = uparrows.resize((100,65))
        uparrows_actual = ImageTk.PhotoImage(uparrows_size)

        downarrows = Image.open("/Users/zaidr/Desktop/Coding/Word-Amount/downarrow.png")
        downarrows_size = downarrows.resize((65,50))
        downarrows_actual = ImageTk.PhotoImage(downarrows_size)



        style = ttk.Style()
        style.theme_use('default')
        style.configure("Custom.TButton", background="#c2f970", foreground='Black', borderwidth='1', focuscolor='none', borderradius=15)

        Label(new, image=startup_actual, background="#DAF1F7").place(x=100, y=50)
        Label(new, image=uparrows_actual, background="#DAF1F7").place(x=180,y=200)
        Label(new, image=downarrows_actual, background="#DAF1F7").place(x=220, y=0)

        Message(new, text="Clears all text so you can make another submission", background="#DAF1F7", font=('Robot', '10')).place(x=150, y=0)
        Message(new, text="This shows the amount of words in a text and the text corrected for grammatical errors", font=('Roboto', '10'),background="#DAF1F7").place(x=60, y=220)
        next = ttk.Button(master=new, text="Next", style="Custom.TButton", command=lambda: new.destroy())
        next.place(x=510)
        new.mainloop()

news = Newscreen(root)
root.mainloop()
