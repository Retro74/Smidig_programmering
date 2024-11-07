biler_dict = {}

while True:
    ny_bil = input("Registrer ny bil: ").capitalize()
    if ny_bil == "":
        break
    if ny_bil in biler_dict: ## Sjekker om merket finnes fra før
        biler_dict[ny_bil] +=1 ## Øker antallet med en
    else:
        biler_dict[ny_bil] = 1 ##Legge inn det nue merket med en bil

print (biler_dict)