

tall = input("Skriv inn ett tall")

try:
    svar = 10/ int(tall)
    print("10/",  tall, "er", svar)

except Exception as unntak:
    print("Du skrev inn",  tall, ", det ble en feil: ", unntak )
