#Hent inn bruker-setning
setning = input("Skriv en setning ")
#Skriv instruksjoner
print("1. Skriv ut setningen i store bokstaver.")
print("2. Skriv ut setningen i små bokstaver.")
print("3. Skriv ut setningen baklengs.")
#Hent inn bruker-valg
valg = input("Hva vil du gjøre (1-3)? ")

#Utfør ustkrift bassert på bruker-valg (1-3) 
if valg == "1":
    print(setning.upper())
elif valg== "2":
    print(setning.lower())
elif valg=="3":
        print(setning[::-1])
else:
    print("Ugyldig valg")