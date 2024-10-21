import pandas
import seaborn as sns
import matplotlib.pyplot as plt

filnavn = "Runde1/Innbyggertall_Byer.csv"
innbyggere_byer_df = pandas.read_csv(filnavn)
# Eksempeldata: "tips" datasett fra Seaborn
#tips = sns.load_dataset("tips")
# Lag en enkel Seaborn graf (f.eks. scatter plot)

sns.barplot(x="By", y="Innbyggertall", data=innbyggere_byer_df)
#print(type(tips))
# Vise grafen
plt.show()
