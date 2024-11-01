import matplotlib.pyplot as plt  # Bibliotek for grafiske framstillinger
import pandas as pd
annuitetslaan_df=  pd.read_csv("Runde1/1.9_MatPlotLib/Annuitetslaan.csv", sep=";", decimal=",")

print(annuitetslaan_df["Renter"].sum())

plt.bar(annuitetslaan_df["År"], annuitetslaan_df["Avdrag"], label="Avdrag")
plt.bar(annuitetslaan_df["År"], annuitetslaan_df["Renter"], label="Renter", bottom=annuitetslaan_df["Avdrag"])

plt.xlabel("År")
plt.ylabel("Kroner")
plt.title(f"Annuitetslån på: {annuitetslaan_df["Avdrag"].sum():.0f} kroner")
plt.legend()

# Vis plot
plt.show()
