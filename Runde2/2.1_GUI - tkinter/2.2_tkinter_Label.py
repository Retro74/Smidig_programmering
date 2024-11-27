from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title("Demonstrasjon av ulike Labels med bakgrunnsfarger")

# Label 1: Standard font og bakgrunnsfarge
Label(root, text="Dette er en standard Label.", background="lightgray").pack(pady=10)

# Label 2: Større font, blå tekst og gul bakgrunn
Label(root, text="Blå tekst, stor font, gul bakgrunn!", font=("Helvetica", 20), foreground="blue", background="yellow").pack(pady=10)

# Label 3: Rød tekst med annen font og hvit bakgrunn
Label(root, text="Dette er en Label med Courier font.", font=("Courier", 16), foreground="red", background="white").pack(pady=10)

# Label 4: Grønn tekst, fet skrift, blå bakgrunn
Label(root, text="Grønn fet tekst, blå bakgrunn!", font=("Arial", 18, "bold"), foreground="green", background="lightblue").pack(pady=10)

# Label 5: Oransje tekst med kursiv stil og svart bakgrunn
Label(root, text="Oransje tekst, kursiv, svart bakgrunn.", font=("Times New Roman", 18, "italic"), foreground="orange", background="black").pack(pady=10)
root.resizable(False, False)
root.mainloop()
