land = [
    "Norge", "Sverige", "Danmark", "Finland", "Island",
    "Tyskland", "Frankrike", "Italia", "Spania", "Portugal",
    "Hellas", "Nederland", "Belgia", "Sveits", "Østerrike",
    "Storbritannia", "Irland", "Polen", "Tsjekkia", "Ungarn",
    "Russland", "Ukraina", "Tyrkia", "Israel", "Japan",
    "Kina", "Sør-Korea", "India", "Pakistan", "Indonesia",
    "Australia", "New Zealand", "Canada", "USA", "Mexico",
    "Brasil", "Argentina", "Chile", "Peru", "Colombia",
    "Sør-Afrika", "Egypt", "Nigeria", "Kenya", "Etiopia",
    "Thailand", "Vietnam", "Malaysia"
]
#Legger til deloppgavene a-c som funksjoner
# slik at de enkelt kan kjøres en og en
def a(): 
    global land
    for i in range(0,len(land), 2):
        land[i], land[i+1] = land[i+1], land[i]
def b(): 
    global land
    for i in range(0,len(land), 3):
        land[i], land[i+1], land[i+2] = land[i+2], land[i], land[i+1]

def c(): 
    global land
    for i in range(0,len(land), 4):
        land[i], land[i+1], land[i+2], land[i+3] = land[i+3], land[i], land[i+1], land[i+2]

def a_c(hopp):
    global land
    for i in range(0,len(land), hopp):
        tmp = land[i+hopp-1] #Tar vare på den som skal flyttes frem
        for j in range(hopp-1,0,-1):# 3, 2, 1 
            land[i+j] = land[i+j-1] #Flytter de som skal flyttes bakover nest bakerst først
        land[i] = tmp #Setter den siste vi tok vare på først

##To alternatover på hver deloppgave 
#a() #Mer kode men enklere. Begrenset til nøyaktige hopp
#a_c(2) #Mindre kode, bare en funksjon for alle. Fungerer for alle hopplengder

#b()
#a_c(3) 

#c()
a_c(4) 
print(land)
