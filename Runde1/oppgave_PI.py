import math


piforsok = str((4297607660/144171)**(1/9))
pi_math = str(math.pi)

print(math.pi)
print (piforsok)

for i in range(len(pi_math)):
    if pi_math[i] != piforsok[i]:
        print(f"De to tallene er like inntil det {i-1}. desimalet, hvor Pi har {pi_math[i]} og brøken har {piforsok[i]}")
        break
