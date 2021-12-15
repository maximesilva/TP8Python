import requests
from InterfaceSearchProvider import InterfaceSearchProvider
from requests import *
from bs4 import BeautifulSoup
from parse import *

class Century21Provider(InterfaceSearchProvider):
    def __init__(self):
        super()
        self.entrypoint = "https://www.century21.fr/annonces/f/achat"
    
    def getSearchResult(self, search):
        if (search["typeAchat"] == "location"):
            self.entrypoint = "https://www.century21.fr/annonces/location"
            search["budgetMin"] = "0"

        url = self.entrypoint + "-" + search["typeBien"] + "/cpv-" + search["codePostal"] + "_" + search["ville"] + "/s-0-/st-0-/"+"/b-" + search["budgetMin"] + "-" + search["budgetMax"] 
        result = requests.get(url)
        print(url)
        bs = BeautifulSoup(result.content, 'html.parser')
        allAnnonces = bs.find_all('div', {'class': 'js-the-list-of-properties-list-property'})
        
        resultSearch = {}
        resultSearch["century21"] = []

        for annonce in allAnnonces:
            annonce = str(annonce)
            parsed = parse('<div{}<a{}detail/{}/{}', annonce)
            reference = parsed[2]

            parsedInformation = parse('{}-bold">{}<br/>{}<sup>2</sup>, {}<div{}>{}</div>{}darker">{} à vendre{}</div>{}<div class="c-text-theme-heading-1{}">{}</div>{}', annonce)
            
            temp = parsedInformation[1].replace('\xa0', '').replace('\n', '').strip(' ')
            ville = temp.split(" ")[0]
            a = len(temp.split(" "))
            cp = temp.split(" ")[a-1]
            superficie = parsedInformation[2].replace('\xa0', '').replace('\n', '').strip(' ')
            temp = parsedInformation[3].replace('\xa0', '').replace('\n', '').strip(' ')
            nbPieces = temp.split(' ')[0]
            temp = parsedInformation[5].replace('\xa0', '').replace('\n', '').strip(' ')
            reference = temp.split(" ")[2]
            typeBien = parsedInformation[7].replace('\xa0', '').replace('\n', '').strip(' ')
            temp = parsedInformation[11].replace('\xa0', '').replace('\n', '').strip(' ')
            prix = temp.split("\u20ac")[0] 

            resultSearch["century21"].append({"reference": reference, "prix": prix, "information" : typeBien +" à "+ ville +" "+ cp +" "+ superficie +" "+ nbPieces +" pièces" })
        
        return resultSearch
    
    def getFileName(self) -> str:
        return "century21"