import kontakter as kontaktfil
print(kontaktfil.kontakter)

for kontakt in kontaktfil.kontakter:
    kontakt["fornavn"] = kontakt["navn"].split(" ")[0]
    kontakt["etternavn"] = kontakt["navn"][len(kontakt["fornavn"])+1:]
    print(kontaktfil.kontakter)