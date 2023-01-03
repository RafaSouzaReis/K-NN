from typing import List

class data:
    def __init__(self, attributes: List[float], classification: str):
        self.__attributes__ = attributes
        self.__classification__ = classification
        self.__distance__: float = 0

    def GetAttributes(self):
        return self.__attributes__

    def GetClassification(self):
        return self.__classification__
    
    def GetDistance(self):
        return self.__distance__
    
    def SetDistance(self, distance: float):
        self.__distance__ = distance