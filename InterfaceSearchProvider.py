from abc import ABC, abstractmethod

class InterfaceSearchProvider(ABC):

    @abstractmethod
    def getSearchResult(self, search):
        pass

    @abstractmethod
    def getFileName(self):
        pass