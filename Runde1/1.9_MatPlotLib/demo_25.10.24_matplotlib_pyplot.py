import matplotlib.pyplot as plt 
import pandas as pd

data = {'Bynavn': ['Oslo', 'Bergen', 'Trondheim', "Harstad"],
        'Innbyggertall': [681067, 280216, 171322, 26431 ]}
df = pd.DataFrame(data)
plt.bar(df["Bynavn"], df["Innbyggertall"])

plt.show()