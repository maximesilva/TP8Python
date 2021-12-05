from Century21Provider import *
from LeboncoinProvider import *
from LefigaroProvider import *
from FileDatabase import *

def askMaisonOrAppartement():
    answer = False 
    while (answer != True):
        typeBien = input("Maison ou appartement ?")
        typeBien = typeBien.lower()

        if (typeBien == "maison" ):
            typeBien = "maison"
            answer = True
        elif (typeBien == "appartement"):
            typeBien = "appartement"
            answer = True
        else:
            print('Veuillez rentrer "maison" ou "appartement".')
        
    return typeBien

def askAchatOrLocation():
    answer = False 
    while (answer != True):
        typeAchat = input("Achat ou location ?")
        typeAchat = typeAchat.lower()

        if (typeAchat == "achat" ):
            typeAchat = "achat"
            answer = True
        elif (typeAchat == "location"):
            typeAchat = "location"
            answer = True
        else:
            print('Veuillez rentrer "achat" ou "location".')
        
    return typeAchat

def main():
    typeAchat = askAchatOrLocation()
    typeBien = askMaisonOrAppartement()
    codePostal = input("Code postal ?")
    ville = input("Ville ?")
    budgetMin = input("Budget minimum ?")
    budgetMax = input("Budget maximum ?")
    search = {"typeAchat": typeAchat, "typeBien": typeBien, "codePostal": codePostal, "ville": ville, "budgetMin": budgetMin, "budgetMax": budgetMax}


    fileDatabase = FileDatabase()

    century21 = Century21Provider(search)
    resultCentury21 = century21.getSearchResult()
    fileDatabase.saveInFile(resultCentury21, "century21")

    #fonctionne si on passe la détection en tant que robot
    #lbc = LeboncoinProvider(search)
    #resultLbc = lbc.getSearchResult()
    #fileDatabase.saveInFile(resultLbc, "lbc")

    lefigaro = LefigaroProvider(search)
    resultLefigaro = lefigaro.getSearchResult()
    fileDatabase.saveInFile(resultLefigaro, "lefigaro")
    
main()