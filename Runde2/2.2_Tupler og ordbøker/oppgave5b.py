import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from pathlib import Path
#Bildene ligger i en egen mappe ved siden av pythonfilen
imagesFolder = "images"
imageFileName = 'kart.jpg' 
filePath = Path(__file__).resolve().parent
fullImagePath =filePath.joinpath(imagesFolder).joinpath(imageFileName)
# Last inn kartbildet

temperaturdata = {
    (245, 270): ("Oslo", 17, "cloudy.png"),       # Oslo
    (60, 320): ("Bergen", 18, "rain.png"),     # Bergen
    (270, 505): ("Trondheim", 6, "cloudy.png"),  # Trondheim
    (450, 900): ("Tromsø", 1, "snow.png"),     # Tromsø
    (55, 220): ("Stavanger", 23, "sun.png"),  # Stavanger
    (130, 150): ("Kristiansand", 24, "sun.png") # Kristiansand
}

# Plott kartbildet som bakgrunn
plt.imshow(mpimg.imread(fullImagePath), extent=[0, 800, 0, 1200])  # Juster extent for å passe kartstørrelsen
farger = ['#3f00bf','#0000ff', '#7f007f', '#ff0000', '#bf003f']

# Legg til bynavn, temperaturer og prikk for hver by
for (x, y), (by, temp, vaerikon) in temperaturdata.items():
    # Fargekoding for temperatur: kaldt er blått, varmt er rødt
    farge = farger[int(temp/5)]
    # Plot prikk på byens posisjon med temperaturfarge
    plt.scatter(x, y, color=farge, s=50)  # 's' bestemmer størrelsen på prikken
    
    # Skriv bynavn og temperatur
    plt.text(x, y + 20, f"{by}: {temp}°C", color="black", fontsize=9, ha='center')

    # Legg til værikon som et lite bilde rett ved byen
    imagePath= filePath.joinpath(imagesFolder).joinpath(vaerikon)
    mpimg_imread_ikon_bilde = mpimg.imread(imagePath)
    ikon_size = 40  # Setter ikonstørrelsen
    ikon_x_offset = 40  #Flytter ikonet litt til høyre for byens koordinater (i x-retning)
    plt.imshow(mpimg_imread_ikon_bilde, extent=(x - ikon_size + ikon_x_offset,
                                   x + ikon_size + ikon_x_offset,
                                   y - ikon_size, 
                                   y + ikon_size))

# Dette er en "walk-around". 
# Ikke pent, men får plt til å vise hele kartet.
# Et siste gjennomsiktige bilde legges til og 
# plasseres over til slutt
clearImage = filePath.joinpath(imagesFolder).joinpath("clear.png")
plt.imshow(mpimg.imread(clearImage), extent=[0, 800, 0, 1200])  # Juster extent for å passe kartstørrelsen

# Skjul akser (valgfritt)
plt.axis('off')

# Vis kartet med temperaturdata
plt.show()