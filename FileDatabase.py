import json
import os

class FileDatabase():
    def __init__(self):

        self.fileName = "searchResult.json"

    def saveInFile(self, newSearchResult, providerName):
        if (os.path.isfile(self.fileName)==False) :  
            with open(self.fileName, 'w') as outfile:
                json.dump(newSearchResult, outfile)
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
                    data[providerName] = []
                    data[providerName].append(newSearchResult)

            os.remove(self.fileName)
            with open(self.fileName, 'w') as outfile:
                json.dump(data, outfile)
                            
            
            
                

