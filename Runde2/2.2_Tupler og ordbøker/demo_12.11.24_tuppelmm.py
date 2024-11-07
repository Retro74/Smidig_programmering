

# Konstanter
NORGES_HOVEDSTAD = "Oslo"
print(NORGES_HOVEDSTAD)
#NORGES_HOVEDSTAD = "Stockholm"
#print(NORGES_HOVEDSTAD)

ukedager = ("mandag", "tirsdag", "onsdag", "torsdag", "fredag", "lørdag", "søndag")
print(ukedager[2])

d1, d2, d3, d4, d5, d6, d7 = ukedager
print(d1)



vinner_USA = "Kamala Harris"
taper_USA = "Donald Trump"
#tmp = vinner_USA
#vinner_USA = taper_USA
#taper_USA = tmp


vinner_USA, taper_USA = taper_USA, vinner_USA
print(vinner_USA)

##vise ZIP
karakter    = [1, 2, 3, 4, 5, 6]
frekvenser  = [1, 3, 6, 5, 3, 2]
#raadata = [1,2,2,2, 3,3,3,3,3,3,4,4,4,4,4,5,5,5,6,6]
frekvenstabell = zip(karakter, frekvenser)
print (*frekvenstabell)
sumKarakter = 0
for karakter, antall in zip(karakter, frekvenser):
    sumKarakter += karakter*antall

gjennomsnitt = sumKarakter/sum(frekvenser)
print("Gjennomsnitt:", gjennomsnitt)