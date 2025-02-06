class Vapen:
    def __init__(self, navn:str, skade:int = 10, ammunisjon:int = 5)->None:
        """Klasse for et våpen

        Args:
            navn (str): våpenets navn
            skade (int, optional): hvor mye skade våpenet gjør. Defaults to 10.
            ammunisjon (int, optional): antall skudd igjen . Defaults to 5.
        """
        self.__navn = navn
        self.__skade = skade
        self.__ammunisjon = ammunisjon
    def skyt(self)-> str:
        """Avfyrer våpenet 
        Reduserer ammunisjon med 1 til tomt 

        Returns:
            str: Returnerer "Bang!" dersom det er mer enn 0 i ammuniasjon, eller "Klikk!"
        """
        if self.__ammunisjon > 0:
            self.__ammunisjon-=1
            return "Bang!"
        else:
            return "Klikk!"
    def ladd_opp(self)-> None:
        """Lader opp, setter ammuniasjon tilbake til 5
        """
        self.__ammunisjon =5


Desert_Eagle = Vapen("Desert Eagle")
print(Desert_Eagle.skyt())
print(Desert_Eagle.skyt())
print(Desert_Eagle.skyt())
print(Desert_Eagle.skyt())
print(Desert_Eagle.skyt())
print(Desert_Eagle.skyt())
Desert_Eagle.ladd_opp()
print(Desert_Eagle.skyt())
print(Desert_Eagle.skyt())
print(Desert_Eagle.skyt())
print(Desert_Eagle.skyt())
print(Desert_Eagle.skyt())
print(Desert_Eagle.skyt())

        
    