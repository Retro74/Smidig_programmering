class Land:
    def __init__(self, navn:str, hovedstad:str, befolkning:int):
        self.__navn= navn
        self.__hovedstad = hovedstad
        self.befolkning = befolkning
    def visInfo(self):
        print(self.navn, self.__hovedstad, self.befolkning)
        



norge = Land("Norge", "Oslo", 5000000)
norge.__hovedstad="Bergen"
norge.visInfo()