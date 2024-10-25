import matplotlib.pyplot as plt
import random as rnd

antObservasjoner = 15

x = [rnd.randint(1,20) for n in range(antObservasjoner)]
y = [rnd.randint(50,120) for n in range(antObservasjoner)]
z = [rnd.randint(5,300) for n in range(antObservasjoner)]
plt.scatter(x, y, s= z)

plt.title("Tilfeldige punkter")

plt.show()
