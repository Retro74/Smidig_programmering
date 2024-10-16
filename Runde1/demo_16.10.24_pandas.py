import pandas
dataframe = pandas.read_csv("Runde1/2019.csv", delimiter=";")
print(dataframe)

#datalist = dataframe.values.tolist()
#print(datalist)

prisliste_SSG_kost_df = dataframe.sort_values(by= "kost", ascending=False)
#print(prisliste_SSG_kost_df)
prisliste_SSG_kost_Top_5_df = prisliste_SSG_kost_df.head(5).fillna("-")
#print(prisliste_SSG_kost_Top_5_df)
#print(type(dataframe))

Europa_df= dataframe[dataframe["verdensdel"]=="Europa"] 
#print(Europa_df)
kost_over_800 = dataframe[dataframe["kost"]>=800].sort_values(by="kost")
#print(kost_over_800)
#print(len(kost_over_800))

#print(kost_over_800[["verdensdel","kost"]])