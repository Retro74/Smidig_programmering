import numpy as np  # Matematisk bibliotek
import matplotlib.pyplot as plt

# Definerer funksjonen
x = np.linspace(-6, 6, 101)
f_av_x = -x**2

colors = ['#ff0000','#ffa500','#ffff00','#008000','#0000ff','#4b0082','#ae32ae']
for i in range(len(colors)):
    plt.plot(x,f_av_x+i/2, color=colors[i])
  
plt.axis('off')
plt.show()