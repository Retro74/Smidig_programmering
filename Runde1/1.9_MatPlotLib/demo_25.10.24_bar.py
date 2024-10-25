import matplotlib.pyplot as plt

spill = ['Fortnite', 'Minecraft', 'Roblox', 'Among Us', 'Valorant']
antall_spillere_mill = [350, 300, 220, 180, 150]  # i millioner
farger = ['#7d3cff', '#ffdb58', '#ff6347', '#00ced1', '#ff4500']  # Lilla, Gul, Tomatrød, Turkis, Oransje

plt.bar(spill, antall_spillere_mill, color=farger)
plt.title("Populære spill i 2024")
plt.xlabel("Spill")
plt.ylabel("Antall spillere i millioner")
plt.show()