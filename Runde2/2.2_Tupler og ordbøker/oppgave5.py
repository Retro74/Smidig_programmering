import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path
fileName = 'kart.jpg' 
filePath = Path(__file__).resolve().parent
fullPath =f"{filePath}\{fileName}"
# Last inn kartbildet

temperaturdata = {
    (245, 270): ("Oslo", 17),       # Oslo
    (60, 320): ("Bergen", 18),     # Bergen
    (270, 505): ("Trondheim", 6),  # Trondheim
    (450, 900): ("Tromsø", 1),     # Tromsø
    (55, 220): ("Stavanger", 23),  # Stavanger
    (130, 150): ("Kristiansand", 24) # Kristiansand
}

# Plott kartbildet som bakgrunn
plt.imshow(mpimg.imread(fullPath), extent=[0, 800, 0, 1200])  # Juster extent for å passe kartstørrelsen
farger = ['#3f00bf','#0000ff', '#7f007f', '#ff0000', '#bf003f']

# Legg til bynavn, temperaturer og prikk for hver by
for (x, y), (by, temp) in temperaturdata.items():
    # Fargekoding for temperatur: kaldt er blått, varmt er rødt
    farge = farger[int(temp/5)]
    # Plot prikk på byens posisjon med temperaturfarge
    plt.scatter(x, y, color=farge, s=50)  # 's' bestemmer størrelsen på prikken
    
    # Skriv bynavn og temperatur
    plt.text(x, y + 20, f"{by}: {temp}°C", color="black", fontsize=9, ha='center')

# Skjul akser (valgfritt)
plt.axis('off')

# Vis kartet med temperaturdata
plt.show()