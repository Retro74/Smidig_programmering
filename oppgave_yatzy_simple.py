import random
terninger = "⚀⚁⚂⚃⚄⚅"

#Kaster 5 terninger
terning1 = random.randint(1,6)
terning2 = random.randint(1,6)
terning3 = random.randint(1,6)
terning4 = random.randint(1,6)
terning5 = random.randint(1,6)

print(terninger[terning1-1], 
      terninger[terning2-1], 
      terninger[terning3-1], 
      terninger[terning4-1], 
      terninger[terning5-1])

kast_paa_nytt = input("Hvilke terninger vil du kaste på nytt? (1-5)") #1,4

#Kaster terninger på nytt
if "1" in kast_paa_nytt:
    terning1 = random.randint(1,6)
if "2" in kast_paa_nytt:
    terning2 = random.randint(1,6)
if "3" in kast_paa_nytt:
    terning3 = random.randint(1,6)
if "4" in kast_paa_nytt:
    terning4 = random.randint(1,6)
if "5" in kast_paa_nytt:
    terning5 = random.randint(1,6)

print(terninger[terning1-1], 
      terninger[terning2-1], 
      terninger[terning3-1], 
      terninger[terning4-1], 
      terninger[terning5-1])

kast_paa_nytt = input("Hvilke terninger vil du kaste på nytt? (1-5)") #1,4

#Kaster terninger på nytt
if "1" in kast_paa_nytt:
    terning1 = random.randint(1,6)
if "2" in kast_paa_nytt:
    terning2 = random.randint(1,6)
if "3" in kast_paa_nytt:
    terning3 = random.randint(1,6)
if "4" in kast_paa_nytt:
    terning4 = random.randint(1,6)
if "5" in kast_paa_nytt:
    terning5 = random.randint(1,6)

print(terninger[terning1-1], 
      terninger[terning2-1], 
      terninger[terning3-1], 
      terninger[terning4-1], 
      terninger[terning5-1])
