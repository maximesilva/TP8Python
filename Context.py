from InterfaceSearchProvider import *

class Context:

    def __init__(self):
        self.interfaces = []

    def register(self, interfaceSearchProvider: InterfaceSearchProvider):
        self.interfaces.append(interfaceSearchProvider)
    
    def getSites(self):
        return self.interfaces