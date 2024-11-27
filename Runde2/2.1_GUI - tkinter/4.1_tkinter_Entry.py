from tkinter import *
from tkinter.ttk import *
def skriv_navn():
    print(f"Hei, {entry_navn.get()}!")

root = Tk()
root.title("Entry-demo")
root.geometry("400x300")

lbl_navn = Label(root, text="Hva heter du?")
lbl_navn .pack()
entry_navn = Entry(root)
entry_navn.pack()

btn_submit = Button(root, text="Vis navn", command=skriv_navn)
btn_submit.pack()

root.mainloop()
