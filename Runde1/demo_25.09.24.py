



#with open("lesmeg.txt") as fil:
#    data = fil.read()
#    #print(data)
#    fil.seek(0)
#    for linje in fil:
#        print(linje, end ="")
#

player1 = "Roger"
topScore1 = 100
player2 = "Siv"
topScore2 = 120

with open("minScore.txt", mode="w", encoding="utf-8") as fil:
    fil.write(player1 + ";" + str(topScore1) + "\n")
    fil.write(player2 + ";" + str(topScore2) + "\n")
    

