from typing import List
from data import data
from newData import newData

import math

class kNearestNeighbors:
    def __init__(self, k: int, dataJoint: List[data]):
        self.__k__ = k
        self.__dataJoint__ = dataJoint

    def __EuclideanDistance__(self, newDataAttributes: List[float], dataClassificationAttributes: List[float]):
        summation: float = 0
        for dataClassificationAttribut,newDataAttribut in zip(dataClassificationAttributes, newDataAttributes):
            summation += math.pow((dataClassificationAttribut - newDataAttribut), 2)
        return math.sqrt(summation)

    def __FindClosest__(self):
        sortJoint: List[data] = sorted(self.__dataJoint__, key = data.GetDistance)
        return sortJoint [:self.__k__]

    def __classificationMostRecurrent__(self, closestData:List[data]):
        dictionaryClassification = {}
        for dataNext in closestData:
            if dataNext.GetClassification() in dictionaryClassification:
                dictionaryClassification[dataNext.GetClassification()] += 1
            else:
                dictionaryClassification[dataNext.GetClassification()] = 1
        return max(dictionaryClassification, key=dictionaryClassification.get)

    def exec(self, newData: newData):
        for classificationData in self.__dataJoint__:
            distance = self.__EuclideanDistance__(newData.GetAttributes(), classificationData.GetAttributes())
            classificationData.SetDistance(distance)
        closestData : List[data] = self.__FindClosest__()
        classification = self.__classificationMostRecurrent__(closestData)
        newData.SetClassification(classification)