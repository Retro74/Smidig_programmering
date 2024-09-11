import random
terninger = "⚀⚁⚂⚃⚄⚅"

#Kaster 5 terninger
terning1 = random.randint(1,6)
terning2 = random.randint(1,6)
terning3 = random.randint(1,6)
terning4 = random.randint(1,6)
terning5 = random.randint(1,6)

terningsett = str(terning1) + str(terning2) + str(terning3) + str(terning4) + str(terning5)
print(terningsett)
print(terninger[terning1-1], 
      terninger[terning2-1], 
      terninger[terning3-1], 
      terninger[terning4-1], 
      terninger[terning5-1])

kast_paa_nytt = input("Hvilke terninger vil du kaste på nytt? (1-5, kommasepparert)") #1,4
kast_paa_nytt = kast_paa_nytt.split(",") # ["1", "4"]

for terningnummer in kast_paa_nytt: # "1"  "4"
    terningnummer = int(terningnummer)
    terningsett = terningsett[:terningnummer-1] + str(random.randint(1,6)) + terningsett[terningnummer:] 


print(terningsett)


