

## Finne nøkler med en gitt verdi

ordbok = {"a": 10, "b": 12, "c": 30, "d":10}

noklermedVerdi10 = [nokkel for nokkel, verdi in ordbok.items() if verdi == 10]
print (noklermedVerdi10)


for nokkel, verdi in ordbok.items():
    print("Nøkkel:", nokkel)
    print("Verdi:", verdi)
