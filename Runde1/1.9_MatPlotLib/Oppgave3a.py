# Importerer ekstra moduler som ikke er standard Python
import matplotlib.pyplot as plt  # Bibliotek for grafiske framstillinger
import numpy as np  # Matematisk bibliotek

# Definerer funksjonen Siden denne funksjonen ikke er definert for x=1,5, lager vi to lister av x-verdier 
x1 = np.linspace(-2, 1.5, 101)
x2 = np.linspace(1.5, 6, 101)
def f_av(x):
    return  (x+1)/(2*x-3)

# Lager grafen inkludert tekst til tekstboks
plt.plot(x1, f_av(x1), color ="blue", label=r"$f\left(x\right)=\frac{x+1}{2x-3}$")
plt.plot(x2, f_av(x2), color ="blue")
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