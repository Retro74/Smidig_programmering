# Importerer ekstra moduler som ikke er standard Python
import matplotlib.pyplot as plt  # Bibliotek for grafiske framstillinger
import numpy as np  # Matematisk bibliotek

# Definerer funksjonen 
x = np.linspace(-5, 6, 101)
def f_av(x):
    return  3*x**3 + 4*x**2 - 3*x + 1

# Lager grafen inkludert tekst til tekstboks
plt.plot(x, f_av(x), color ="blue", label=r"$g\left(x\right)=3x^3+4x^2-3x+1$")
# Med dollartegn $ får vi penere matematisk notasjon

# Slår på rutenett
plt.grid(True) 

# Tar bort høyre og øvre akse og lar aksene krysse hverandre i (0, 0)
plt.gca().spines['right'].set_visible(False)
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['bottom'].set_position("zero")
plt.gca().spines['left'].set_position("zero")

# Lager aksetitler
plt.xlabel("$x$") # Tittel på x-aksen
plt.ylabel("$y$", rotation=0)
plt.gca().yaxis.set_label_coords(0.3,1)
plt.gca().xaxis.set_label_coords(1,0.23)

# Lager tekstboks med funksjonsuttrykk
plt.legend(bbox_to_anchor=(0.6,0.5))

# Tegner grafen
plt.show()