import datetime
aktiviteter = ["1. Surfer på vg.no", "2. Jobbet med R2-lekser", "3. Flørtet med kjæresten på nettet"]
with open("Runde1/aktivitet.txt", "a", encoding='utf-8') as fil:
    ##fil.write("#hehe")
    while True:
        print("\nHva vil du gjøre?")
        print("1. Loggføre en aktivitet")
        print("2. Vise statistikk")
        print("q. Avslutte programmet")
        valg = input("Ditt valg: ")

        if valg == '1':
            while True:
                print("Velg aktivitet")
                for aktivitetsValg in aktiviteter:
                    print(aktivitetsValg)
                print("q. Avslutt loggføring")
                aktivitetNummer = input("Ditt valg: ")
                aktivitetsstart = datetime.datetime.now() 
                print (aktivitetsstart)
                if aktivitetNummer.lower()=="q":
                    break
                input(f"Avslutt {aktiviteter[int(aktivitetNummer)-1]}")
                fil.write(aktiviteter[int(aktivitetNummer)-1] + ";"+ str(aktivitetsstart) + ";" + str(datetime.datetime.now()) )


        elif valg == '2':
            vis_statistikk()
        elif valg.lower() == 'q':
            print("Farvel!")
            break
        else:
            print("Ugyldig valg. Prøv igjen.")

