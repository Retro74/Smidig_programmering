from tkinter import *
from tkinter.ttk import *

def knapp_trykket():
    print("Knappen er trykket!")

root = Tk()
root.title("Button-demo")
root.geometry("400x300")
btn_action = Button(root, text="Klikk meg!", command=knapp_trykket)
btn_action.pack()

root.mainloop()
