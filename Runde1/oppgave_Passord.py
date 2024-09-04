passord = "QBTTPSE234"   #Hemmelig: "PASSORD123"
nokkel = "abcdefghijklmnopqrstuvwxyzæøå1234567890.,;:".upper()
kryptertPassord =""
for i in range(len(passord)):
    kryptertPassord += nokkel[nokkel.index(passord[i])-1]

#print(kryptertPassord)
gjettet_passord = input("Passord: ")

print(kryptertPassord)
while gjettet_passord != kryptertPassord:
    gjettet_passord = input("Feil passord skriv inn på nytt: ")

print("Velkommen!")
