class Oppskrift:
    def __init__(self, navn:str, ingredienser:list, tid:int, fremgangsmaate:str):
        """Klasse for oppskrift
        Args:
            navn (str): oppskriftens navn
            ingredienser (list): liste med ingedienser [["ingrdiens", "mengde":float, "enhet"],]
            tid (int): tilberdingstid i minutter
        """
        self.__navn = navn
        self.__ingredienser = ingredienser
        self.__tid = tid
        self.__fremgangsmaate = fremgangsmaate
    def vis_oppskrift(self, ant_posjoner:int=1):
        print(f"{self.__navn} ({ant_posjoner} posjoner)")
        for ingrdiens in self.__ingredienser:
            print(ingrdiens[0], ingrdiens[1]*ant_posjoner, ingrdiens[2])
        print("Fremgangsmåte: ", self.__fremgangsmaate)
        print("Tilberdingstid: ", self.__tid, "minutter")
    
    def legg_til_ingrediens(self, navn:str, mengde:float, enhet:str):
        if navn != "" and mengde > 0 and enhet != "":
            self.__ingredienser.append([navn, mengde, enhet])
    
    def slett_ingrediens(self, slettIngrediens_navn):
        for i in range(len(self.__ingredienser)-1,0,-1):
            if self.__ingredienser[i][0]== slettIngrediens_navn:
                self.__ingredienser.pop(i)

class VegetarOppskrift(Oppskrift):
    def __init__(self, navn, ingredienser, tid, fremgangsmaate):
        self.__veganvennlig = True 
        super().__init__(navn, ingredienser, tid, fremgangsmaate)
    def vis_oppskrift(self, ant_posjoner:int=1):
        print("Denne oppskriften er vegansk")
        super().vis_oppskrift(ant_posjoner)
 
class DessertOppskrift(Oppskrift):
    def __init__(self, navn, ingredienser, tid, fremgangsmaate, antall_kalorier:int):
        super().__init__(navn, ingredienser, tid, fremgangsmaate)
        self.antall_kalorier = antall_kalorier
    def vis_oppskrift(self, ant_posjoner:int=1):
        print(f"Denne oppskriften inneholder totalt {self.antall_kalorier*ant_posjoner}kcal, ({self.antall_kalorier} kcal pr. pers.)")
        super().vis_oppskrift(ant_posjoner)

spagettiBolognese = Oppskrift("Spagetti Bolognese", [["Løk", 1/2, "stk"], 
                                                     ["Kjøttdeig", 80, "g"], 
                                                     ["Pasta/Spagetti", 100, "g"],
                                                     ["Hvitløk", 1/2, "fed"],
                                                     ["Tomatsaus", 1.5, "dl"]], 30, 
                                                     "Kok pasta i 10 minutter. Stek kjøttdeig og løk. Hell i tomatsaus. La kokse i 15 minutter. Server varmt, gjerne med revet parmesan på toppen.")
spagettiBolognese.legg_til_ingrediens("Basilikum", 3 , "blader")
spagettiBolognese.slett_ingrediens("Hvitløk")

spagettiBolognese.vis_oppskrift(2)
veganskSpagettiBolognese = VegetarOppskrift("Vegansk Spagetti Bolognese", [["Løk", 1/2, "stk"], 
                                                     ["Soyabasert kjøttdeigserstatning", 80, "g"], 
                                                     ["Pasta/Spagetti", 100, "g"],
                                                     ["Hvitløk", 1/2, "fed"],
                                                     ["Tomatsaus", 1.5, "dl"]], 30, 
                                                     "Kok pasta i 10 minutter. Stek kjøttdeig og løk. Hell i tomatsaus. La kokse i 15 minutter. Server varmt, gjerne med revet parmesan på toppen.")
#veganskSpagettiBolognese.vis_oppskrift()
tiramisu = DessertOppskrift("Tiramisu", [["Eggeplomme", 0.5, "stk"], 
                                         ["Sukker", 0.5, "ss"],
                                         ["Mascarponeost", 50, "g"],
                                         ["Eggehvite", 0.5, "stk"],
                                         ["Fingerkjeks", 3, "stk"],
                                         ["Espressokaffe", 0.5,"dl"],
                                         ["Konjakk", 1, "ts"]], 35, 
                                         "Bland eggeplommer med sukker og pisk luftig, tilsett mascarpone og rør glatt.\n2. Pisk eggehvitene stive med en klype salt. Vend eggehvitene inn i ostekremen med en slikkepott.\n3. Legg et lag med krem i bunnen av en serveringsskål. Dypp fingerkjeksene raskt i kaffe, blandet med konjakk (pass på så dem ikke blir for bløte) og legg dem på kremen.\n4. Legg et nytt lag med krem, kjeks oppå og avslutt med et lag krem. Dryss revet sjokolade på toppen og avkjøl ca. 1 time før servering.", 415)

#tiramisu.vis_oppskrift(4)