#Hent inn en tekst
tekst = input("Skriv inn en tekst: ")
if tekst == "":
    print("Tom tekst")
    exit()

# Setter initielle variabler 
antallTeller = 1
rle_tekst = ""

#Går gjennom teksten som er sendt inn tegn for tegn (fra index 1)
for i in range(1, len(tekst)):
    #Er det tegnet som undersøkes den samme som forrige?
    if tekst[i]==tekst[i-1]:
        antallTeller+=1
    else:
        #Hvis ikke samme tegn skriv antall og det forrige tegnet 
        # og sett antall av nytt tegn lik 1
        rle_tekst += str(antallTeller) + tekst[i-1]
        antallTeller = 1
#Få med siste tegn og antall av det
rle_tekst += str(antallTeller) + tekst[-1]
#Skriv ut komprimert streng
print(rle_tekst)