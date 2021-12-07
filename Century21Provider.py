import requests
from InterfaceSearchProvider import InterfaceSearchProvider
from requests import *
from bs4 import BeautifulSoup
from parse import *

class Century21Provider(InterfaceSearchProvider):
    def __init__(self):
        super()
        self.entrypoint = "https://www.century21.fr/annonces/achat"
    
    def getSearchResult(self, search):
        if (search["typeAchat"] == "location"):
            self.entrypoint = "https://www.century21.fr/annonces/location"
            search["budgetMin"] = "0"

        url = self.entrypoint + "-" + search["typeBien"] + "/cpv-" + search["codePostal"] + "_" + search["ville"] + "/b-" + search["budgetMin"] + "-" + search["budgetMax"] 
        result = requests.get(url)
        
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
    
    def getFileName(self) -> str:
        return "century21"