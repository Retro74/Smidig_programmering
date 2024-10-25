import matplotlib.pyplot as plt
import numpy as np

def f_av(x):
    return 2*x**2 + 2*x -3

x = np.linspace(-10, 10, 100)
y = f_av(x)

plt.plot(x,y, label=r"$f(x) = 2x^2+2x-3$", color = "darkgreen")
plt.legend()
plt.title(r"Graf av funksjonen: $f(x) = 2x^2+2x-3$")
plt.axvline(0, color="black", linewidth = 2)
plt.axhline(0, color="black", linewidth = 2)

plt.grid()
plt.show()
