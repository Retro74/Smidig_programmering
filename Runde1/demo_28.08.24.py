
#sitat= "I have a dream"

#print(sitat.index("a"))


pi = "3,14"
pi = pi.replace(",", ".")
pi = float(pi)
#pi = 3.14

radius = float((input("Skriv inn en radius")).replace(",","."))
omkrets = 2 * pi * radius
print("Omkretsen er: " + str(round(omkrets,1)))

