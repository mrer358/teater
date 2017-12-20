from  Tkinter import *
import tkMessageBox
from termcolor import colored
class StartSoftware():
    def __init__(self):
        self.root = Tk()
        self.root.geometry("500x500")
        self.root.title("Michael Project Theater")
        self.leble = Label(self.root, text="Telcome To Theater", bg="#fa4219", font=25)
        self.leble.place(x=185,y=0)
        self.root.configure(background="#fa4219")
        self.root.minsize(height=500,width=500)
        self.root.maxsize(height=500,width=500)
        self.listbox = Listbox(self.root,  height=20, width=35, bg="#6f6f6f")
        self.listbox.bind('<<ListboxSelect>>', self.Ce)
        self.listbox.place(x=0,y=40)
        self.button = Button(self.root, text="Exit", bg="#7d8282" ,command=self.Exit)
        self.button.place(x=400, y=450)
        self.button_log = Button(self.root, text="insert a client", bg="#7d8282", command=self.datainsert)
        self.button_log.place(x=352, y=40)
        self.leb1 = Label(self.root, text="name client:", bg="#fa4219")
        self.leb1.place(x=285,y=125)
        self.leb2 = Label(self.root, text="ID number:", bg="#fa4219")
        self.leb2.place(x=285,y=190)
        self.leb3 = Label(self.root, text="number of the chair:",bg="#fa4219")
        self.leb3.place(x=285,y=250)
        self.emy1 = Entry(self.root)
        self.emy1.place(x=285, y=150)
        self.emy2 = Entry(self.root)
        self.emy2.place(x=285, y=210)
        self.emy3 = Entry(self.root)
        self.emy3.place(x=285, y=270)

        mainloop()



    def Exit(self):
        exit()

    def datainsert(self):
        name = self.emy1.get()
        idnumber= self.emy2.get()
        numberofchair= self.emy3.get()
        data = "name: "+  name+ " ID: " +  idnumber  + " chair Catch: " +  numberofchair
        self.listbox.insert(END, data)




    def Ce(self, w):
        exevalue = self.listbox.curselection()
        dataexe = exevalue
        print exevalue
        for d in exevalue:
            self.listbox.delete(exevalue, exevalue)







start = StartSoftware()

def main():
    start
main()
