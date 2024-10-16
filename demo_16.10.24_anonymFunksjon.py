def ordLengde(ord):
    return len(ord)

#print(ordLengde("oslo"))
norskeByer = ["Oslo", "Trondheim", "Harstad", "Tromsø", "Bergen"]
#norskeByer.sort(key=ordLengde)
norskeByer.sort(key= lambda by: len(by))
#print(norskeByer)


norskeByerInnbyggere = [["Oslo",        634293], 
                        ["Trondheim",   182035], 
                        ["Harstad",     3860], 
                        ["Tromsø",      41950], 
                        ["Bergen",      271949]]


norskeByerInnbyggere.sort(reverse=True, key = lambda by: by[1])
print(norskeByerInnbyggere)
