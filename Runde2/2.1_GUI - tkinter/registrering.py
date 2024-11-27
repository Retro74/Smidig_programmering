from tkinter import *
from tkinter.ttk import *

root = Tk()  # Opprett hovedvindu
root.title("Registrering")
root.geometry("400x300")
rowCounter = 0
lbl_title = Label(root, text="Registrering", font=("Arial", 16))
lbl_title.grid(row=rowCounter, column=0, columnspan=2, pady=10)

rowCounter+=1
lbl_fornavn= Label(root, text="Fornavn:")
lbl_fornavn.grid(row=rowCounter, column=0, sticky=E, padx=5, pady=10)
entry_fornavn = Entry(root, width=40)
entry_fornavn.grid(row=rowCounter, column=1, sticky=W, padx=5, pady=10)

rowCounter+=1
lbl_etternavn= Label(root, text="Etternavn:")
lbl_etternavn.grid(row=rowCounter, column=0, sticky=E, padx=5, pady=10)
entry_etternavn = Entry(root, width=40)
entry_etternavn.grid(row=rowCounter, column=1, sticky=W, padx=5, pady=10)
root.mainloop()  # Kjør hovedløkken
