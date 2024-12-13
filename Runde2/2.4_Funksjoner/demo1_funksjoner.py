


def hilsen(fornavn, etternavn="ukjent"):
    global alder 
    return f"Hei, {fornavn} {etternavn} ({alder})"

firstname = "Roger"
surname = "Mikalsen"
alder = 39
minhilsen = hilsen(firstname, surname)
print(alder)
print(minhilsen)