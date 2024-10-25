import matplotlib.pyplot as plt

plattformer = ['TikTok', 'Instagram', 'Snapchat', 'YouTube', 'Facebook']
timer_per_uke = [15, 12, 10, 8, 3]  # Gjennomsnittlig antall timer per uke
farger = ['#69c9d0', '#c13584', '#fffc00', '#ff0000', '#1877f2']  

plt.barh(plattformer, timer_per_uke, color=farger)
plt.title("Tidsbruk på sosiale medier")
plt.xlabel("Timer pr uke")
plt.ylabel("Platformer")
plt.show()