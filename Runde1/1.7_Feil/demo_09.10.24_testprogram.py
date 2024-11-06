def aldersgruppe(alder):
    if alder < 15:
        return "barn"
    elif alder < 67:
        return "voksen"
    else:
        return "pensjonist"



assert aldersgruppe(10)=="barn"
assert aldersgruppe(15)=="voksen"
assert aldersgruppe(20)=="voksen"
assert aldersgruppe(50)=="voksen"
assert aldersgruppe(67)=="pensjonist"
