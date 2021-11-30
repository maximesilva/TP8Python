import requests
from InterfaceSearchProvider import InterfaceSearchProvider
from requests import *
from bs4 import BeautifulSoup
from parse import *

class Century21Provider(InterfaceSearchProvider):
    def __init__(self, search):

        super()
        self.search = search
        self.entrypoint = "https://www.century21.fr/annonces/"
    
    def getSearchResult(self):
        url = self.entrypoint + self.search["typeAchat"] + "/cpv-" + self.search["codePostal"] + "_" + self.search["ville"] + "/b-" + self.search["budgetMin"] + "-" + self.search["budgetMax"] 
        result = requests.get(url)
        bs = BeautifulSoup(result.content, 'html.parser')
    
        allAnnonces = bs.find_all('div', {'class': 'md:tw-grid md:tw-grid-cols-2'})
        resultSearch = {}
        resultSearch["century21"] = []
        for annonce in allAnnonces:
            annonce = str(annonce)
            parsed = parse('{}-bold">{}<br/>{}<sup>2</sup>, {}<div{}>{}</div>{}darker">{} à vendre{}</div>{}<div class="c-text-theme-heading-1{}">{}</div>{}', annonce)
            temp = parsed[1].replace('\xa0', '').replace('\n', '').strip(' ')
            ville = temp.split(" ")[0]
            a = len(temp.split(" "))
            cp = temp.split(" ")[a-1]
            superficie = parsed[2].replace('\xa0', '').replace('\n', '').strip(' ')
            temp = parsed[3].replace('\xa0', '').replace('\n', '').strip(' ')
            nbPieces = temp.split(' ')[0]
            temp = parsed[5].replace('\xa0', '').replace('\n', '').strip(' ')
            reference = temp.split(" ")[2]
            typeBien = parsed[7].replace('\xa0', '').replace('\n', '').strip(' ')
            temp = parsed[11].replace('\xa0', '').replace('\n', '').strip(' ')
            prix = temp.split("\u20ac")[0] 
            resultSearch["century21"].append({"ville": ville, "cp":cp, "superficie": superficie, "nbpieces" : nbPieces, "reference": reference, "typebien": typeBien, "prix": prix})
        
        return resultSearch
        