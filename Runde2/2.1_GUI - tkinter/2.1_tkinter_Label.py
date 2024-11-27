from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Label-demo")
root.geometry("400x300")


lbl_hilsen = Label(root, text="Velkommen til Tkinter!")
lbl_hilsen.pack()
lbl_hilsen.config(text="Heisann")


Label(root, text="Nå skal vi lære om Tkinter!").pack()

root.mainloop()
