


kontakter = [{
    "navn": "Kjell Olsen",
    "alder" : 35,
    "telefonnummer": "+4799234562",
    },{
    "navn": "Morten Iversen",
    "alder" : 33,
    "telefonnummer": "+479923123",
}, ]

print (kontakt["navn"])
print (kontakt["alder"])

kontakt["alder"] = 34
print (kontakt["alder"])

kontakt["fornavn"] = "Kjell"
kontakt["etternavn"] = "Olsen"

print (kontakt["fornavn"])
print (kontakt["etternavn"])

del kontakt["navn"]

print(kontakt)