import json
import os

class FileDatabase():
    def __init__(self):

        self.fileName = "searchResult.json"

    def saveInFile(self, newSearchResult, providerName):
        #Création d'un fichier de sauvegarde si il n'existe pas déjà (première recherche) au format JSON
        if (os.path.isfile(self.fileName)==False) :  
            with open(self.fileName, 'w') as outfile:
                json.dump(newSearchResult, outfile)
        #sinon je réécris le fichier de sauvegarde avec l'ancienne recherche + la nouvelle au format JSON
        else:
            with open(self.fileName) as json_file:
                data = json.load(json_file)

                if (providerName in data):
                    for newSearch in newSearchResult[providerName]:
                        presente = False

                        for annonce in data[providerName]:
                            if (annonce['reference'] == newSearch['reference']):
                                presente = True

                        if presente == False :
                            data[providerName].append(newSearch)
                else:
                    print(newSearchResult)
                    data[list(newSearchResult)[0]] = newSearchResult[providerName]

            os.remove(self.fileName)
            with open(self.fileName, 'w') as outfile:
                json.dump(data, outfile)
                            
            
            
                

