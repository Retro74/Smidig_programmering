pris = int(input("Hva koster varen? "))
betalt = int(input("Hvilken seddel betaler han med? "))
while betalt<pris:
    betalt += int(input("Be kunden betale mer "))
vekslepenger = betalt - pris

print("Kunden skal ha tilbake:", vekslepenger, "kr")