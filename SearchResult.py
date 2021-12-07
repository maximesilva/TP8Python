from Century21Provider import *
from LeboncoinProvider import *
from LefigaroProvider import *
from FileDatabase import *
from Context import *

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

def boot() -> Context :
    context = Context()

    context.register(LefigaroProvider())
    context.register(Century21Provider())
    #context.register(LeboncoinProvider())

    return context

def main():

    context = boot()

    typeAchat = askAchatOrLocation()
    typeBien = askMaisonOrAppartement()
    codePostal = input("Code postal ?")
    ville = input("Ville ?")
    budgetMin = input("Budget minimum ?")
    budgetMax = input("Budget maximum ?")
    search = {"typeAchat": typeAchat, "typeBien": typeBien, "codePostal": codePostal, "ville": ville, "budgetMin": budgetMin, "budgetMax": budgetMax}

    fileDatabase = FileDatabase()

    for site in context.getSites():
        fileDatabase.saveInFile(site.getSearchResult(search), site.getFileName())
    
main()