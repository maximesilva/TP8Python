import requests
from InterfaceSearchProvider import InterfaceSearchProvider
from requests import *
from bs4 import BeautifulSoup
from parse import *

class LefigaroProvider(InterfaceSearchProvider):
    def __init__(self):
        super()
        self.entrypoint = "https://immobilier.lefigaro.fr/annonces/immobilier-vente-bien-"
    
    def getSearchResult(self, search):
        if (search["typeAchat"] == "location"):
            self.entrypoint = "https://immobilier.lefigaro.fr/annonces/immobilier-location-bien-"
        
        url = self.entrypoint + search["ville"] + "+" + search["codePostal"] + ".html?priceMax=" + search["budgetMax"] + "&priceMin=" + search["budgetMin"]
        result = requests.get(url)
        print(url)
        bs = BeautifulSoup(result.content, 'html.parser')
        allAnnonces = bs.find_all('div', {'data-e2e': 'bloc-list-item'})
        
        resultSearch = {}
        resultSearch["lefigaro"] = []

        for annonce in allAnnonces:
            annonce = str(annonce)
            parsed = parse('<div{}id="list-item-{}"{}', annonce)
            uriAnnonce = parsed[1]
            resultSearch["lefigaro"].append({"reference" : uriAnnonce})

        return resultSearch
    
    def getFileName(self) -> str:
        return "lefigaro"