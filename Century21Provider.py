import requests
from InterfaceSearchProvider import InterfaceSearchProvider
from requests import *
from bs4 import BeautifulSoup
from parse import *

class Century21Provider(InterfaceSearchProvider):
    def __init__(self, search):

        super()
        self.search = search
        self.entrypoint = "https://www.century21.fr/annonces/achat"
    
    def getSearchResult(self):
        if (self.search["typeAchat"] == "location"):
            self.entrypoint = "https://www.century21.fr/annonces/location"
            self.search["budgetMin"] = "0"

        url = self.entrypoint + "-" + self.search["typeBien"] + "/cpv-" + self.search["codePostal"] + "_" + self.search["ville"] + "/b-" + self.search["budgetMin"] + "-" + self.search["budgetMax"] 
        result = requests.get(url)
        print(url)
        bs = BeautifulSoup(result.content, 'html.parser')
        allAnnonces = bs.find_all('div', {'class': 'c-the-property-thumbnail-with-content__col-left tw-relative'})
        
        resultSearch = {}
        resultSearch["century21"] = []

        for annonce in allAnnonces:
            annonce = str(annonce)
            parsed = parse('<div{}<a{}detail/{}/{}', annonce)
            reference = parsed[2]
            resultSearch["century21"].append({"reference": reference})
        
        return resultSearch
        