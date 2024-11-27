from pathlib import Path

def get_list_postnummer_poststed():
    fileName = 'Postnummer.csv'
    pyFilePath = Path(__file__).resolve().parent
    fullFilePath = pyFilePath.joinpath(fileName)
    dict_fileData = {}
    with open(fullFilePath) as fil:
        overskrift=fil.readline()
        for linje in fil:
            tmp = linje.strip().split(";")
            dict_fileData[tmp[0]]=tmp[1]
    return dict_fileData

#print(get_list_postnummer_poststed())
