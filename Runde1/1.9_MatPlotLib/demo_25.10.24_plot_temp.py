import matplotlib.pyplot as plt

dager = ["Mandag", "Tirsdag", "Onsdag", "Torsdag", "Fredag", "Lørdag", "Søndag"]
temperaturer = [10, 11, 13, 10, 9, 13, 14]

plt.plot(dager, temperaturer, color="#FF0000", marker="o", linewidth= 2, markersize=16)

plt.title("Temperaturer uke 42")
plt.xlabel("Uke dager")
plt.ylabel("Temp. i C")
plt.grid()
plt.show()
