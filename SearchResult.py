from Century21Provider import *
from LeboncoinProvider import *
from FileDatabase import *

def main():
    # typeAchat = input("Achat ou location ?")
    # typeBien = input("Maison ou appartement ?")
    # codePostal = input("Code postal ?")
    # ville = input("Ville ?")
    # budgetMin = input("Budget minimum ?")
    # budgetMax = input("Budget maximum ?")
    search = {"typeAchat": "achat", "typeBien": "maison", "codePostal": "26000", "ville": "valence", "budgetMin": "0", "budgetMax": "600000"}


    fileDatabase = FileDatabase()

    century21 = Century21Provider(search)
    resultCentury21 = century21.getSearchResult()
    fileDatabase.saveInFile(resultCentury21, "century21")

    lbc = LeboncoinProvider(search)
    resultLbc = lbc.getSearchResult()
    fileDatabase.saveInFile(resultLbc, "lbc")
    
main()