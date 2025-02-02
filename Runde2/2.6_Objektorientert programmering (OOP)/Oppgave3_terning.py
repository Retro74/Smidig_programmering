import random as rnd
class Terning:
    def __init__(self, antallSider:int=6):
        self._antallSider = antallSider
    def trillTerning(self):
        return rnd.randint(1,self._antallSider)
    

minTerning = Terning()
for i in range(10):
    print(minTerning.trillTerning())

min_20_sider_terning = Terning(20)
for i in range(10):
    print(min_20_sider_terning.trillTerning())
        