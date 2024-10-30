import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "Mai", "Jun", "Jul", "Aug", "Sep", "Okt", "Nov", "Des"]
temps_Oslo_2030 = [1.5, 3.2, 6.7, 11.3, 15.7, 19.8, 21.7, 21.3, 17.5, 11.9, 5.6, 2.5]

farger = ['#0000ff', '#3f00bf', '#7f007f', '#bf003f', '#ff0000']

plt.xlabel("Måneder")
plt.ylabel("Temperatur (C)")
plt.title("Gjennomsnittlig temperatur i Oslo gjennom året")

for i in range(1, len(months)):
    gjennomsnittlig_temp = (temps_Oslo_2030[i-1]+temps_Oslo_2030[i])/2
    farge = farger[int(gjennomsnittlig_temp/5)]
    print(temps_Oslo_2030[i-1:i+1])
    plt.plot(months[i-1:i+1], temps_Oslo_2030[i-1:i+1], color= farge)

plt.show()

