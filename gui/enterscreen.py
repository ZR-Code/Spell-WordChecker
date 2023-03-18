from tkinter import *

master = Tk()


class Newscreen:
    def __init__(self, main):
        self.main = main
        main.title("Spell and Word Checker")
        main.resizable(False, False)
        main.geometry("600x300")
        main.configure(background="#DAF1F7")


        self.getstarted = Label(master,text="Get Started", background="#DAF1F7", font=("Comfortaa", 36), foreground="Black").place(x=198, y =10)
        self.tutorial = Button(master=master, text="Tutorial", background="Orange", command=self.tut).place(x=100, y=120)
        self.jumpin = Button(master=master, text="Jump In", bg="Light Green", command=lambda : master.quit()).place(x=350, y= 120)


    def tut(self):
        master.destroy()
        new = Tk()
        new.geometry("600x300")
        new.title("Spell and Word Checker")
        new.resizable(False, False)
        new.mainloop()


news = Newscreen(master)
master.mainloop()
