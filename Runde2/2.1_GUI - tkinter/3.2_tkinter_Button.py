from tkinter import *
from tkinter.ttk import *
tekster = ["Au!", "Kutt ut", "Gi deg!", "Hold opp!"]

teller = 0

def knapp_trykket():
    global teller
    global tekster
    btn_action.config(text=tekster[teller] )
    teller +=1
    if teller >= len(tekster):
        teller=0

root = Tk()
root.title("Button-demo")
root.geometry("400x300")


btn_action = Button(root, text="Ikke klikk på meg!", command=knapp_trykket)
btn_action.pack()

root.mainloop()
