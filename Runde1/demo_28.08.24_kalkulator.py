
tall1 = float(input("Skriv inn ett tall "))
regneart = input("Skriv inn en regneart (+, -, *, /)")
tall2 = float(input("Skriv inn ett tall til "))

if regneart == "+":
    print(tall1 , "+" , tall2, "=", (tall1+tall2))
elif regneart == "-":
    print(tall1 , "-" , tall2, "=", (tall1-tall2))
elif regneart == "*":
    print(tall1 , "*" , tall2, "=", (tall1*tall2))
elif regneart == "/":
    print(tall1 , "/" , tall2, "=", (tall1/tall2))
else: 
    print("Ukjent regneart, " + regneart)

