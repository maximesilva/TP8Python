import requests
from InterfaceSearchProvider import InterfaceSearchProvider
from requests import *
from bs4 import BeautifulSoup
from parse import *

class LeboncoinProvider(InterfaceSearchProvider):
    def __init__(self, search):

        super()
        self.search = search
        self.entrypoint = "https://www.leboncoin.fr/recherche?category="
    
    def getSearchResult(self):
        if (self.search["typeAchat"] == "achat"):
            self.search["typeAchat"] = "9"
        
        url = self.entrypoint + self.search["typeAchat"] + "&locations=" + self.search["codePostal"] + "&price=" + self.search["budgetMin"] + "-" + self.search["budgetMax"]
        result = requests.get(url)
        bs = BeautifulSoup(result.content, 'html.parser')

        allAnnonces = bs.find_all('a', {'data-qa-id': 'aditem_container'})
        
        resultSearch = {}
        resultSearch["lbc"] = []

        for annonce in allAnnonces:
            annonce = str(annonce)
            parsed = parse('{}href="{}>{}', annonce)
            uriAnnonce = parsed[1]
            resultSearch["lbc"].append({"reference" : uriAnnonce})

        print(resultSearch)
        return resultSearch