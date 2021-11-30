from abc import ABC, abstractmethod

class InterfaceSearchProvider(ABC):
    @abstractmethod
    def __init__(self, search):
        
        self.search = search 

    @abstractmethod
    def getSearchResult(self):
        pass