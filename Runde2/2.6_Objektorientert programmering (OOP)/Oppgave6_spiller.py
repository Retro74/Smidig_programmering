class Spiller:
    def __init__(self, navn, level, poeng):
        self.navn = navn
        self.level  = level 
        self.poeng = poeng
    def oppgrader_level(self):
        self.level += 1
        self.poeng += 500

    def gi_bonus(self, bonus):
        self.poeng += bonus
    def __str__(self):
        return ", ".join(f"{planetegnskap}={planetegnskap_verdi}" for planetegnskap, planetegnskap_verdi in vars(self).items())
 

spiller1 = Spiller("Player_1", 5, 1200)
spiller2 = Spiller("Player_2", 3, 800)
spiller3 = Spiller("Player_3", 7, 2000)
print(spiller1)
print(spiller2)
print(spiller3)

spiller1.oppgrader_level()
spiller2.gi_bonus(1000)
print("Etter endring")
print(spiller1)
print(spiller2)
print(spiller3)
