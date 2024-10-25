import matplotlib.pyplot as plt

sportstyper = ['Fotball', 'Basketball', 'E-sport', 'Svømming', 'Ski']
#andeler = [35, 20, 25, 10, 10]  # prosentandel
antall = [117, 45, 33, 21, 15]
farger = ['#34c924', '#ff8c00', '#8a2be2', '#1e90ff', '#dcdcdc']  # Grønn, Oransje, Lilla, Blå, Lys grå

plt.pie(antall, labels=sportstyper, colors=farger, autopct='%1.1f%%', startangle=90)
plt.show()