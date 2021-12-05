import requests
from InterfaceSearchProvider import InterfaceSearchProvider
from requests import *
from bs4 import BeautifulSoup
from parse import *

class LefigaroProvider(InterfaceSearchProvider):
    def __init__(self, search):

        super()
        self.search = search
        self.entrypoint = "https://immobilier.lefigaro.fr/annonces/immobilier-vente-bien-"
    
    def getSearchResult(self):
        if (self.search["typeAchat"] == "location"):
            self.entrypoint = "https://immobilier.lefigaro.fr/annonces/immobilier-location-bien-"
        
        url = self.entrypoint + self.search["ville"] + "+" + self.search["codePostal"] + ".html?priceMax=" + self.search["budgetMax"] + "&priceMin=" + self.search["budgetMin"]
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