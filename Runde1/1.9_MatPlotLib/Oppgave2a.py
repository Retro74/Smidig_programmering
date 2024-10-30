import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Des"]
temps_Oslo_2030 = [1.5, 3.2, 6.7, 11.3, 15.7, 19.8, 21.7, 21.3, 17.5, 11.9, 5.6, 2.5]

plt.xlabel("Måneder")
plt.ylabel("Temperatur (C)")
plt.title("Gjennomsnittlig temperatur i Oslo gjennom året")

plt.plot(months, temps_Oslo_2030)
plt.show()

