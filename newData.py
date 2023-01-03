from typing import List

class newData:
    def __init__(self, attributes: List[float]):
        self.__attributes__ = attributes
        self.__classification__ = None

    def GetAttributes(self):
        return self.__attributes__

    def GetClassification(self):
        return self.__classification__
    
    def SetClassification(self, classification: str):
        self.__classification__ = classification