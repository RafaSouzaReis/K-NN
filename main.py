from typing import List
from data import data
from newData import newData
from kNearestNeighbors import kNearestNeighbors

if __name__ == '__main__':
    dataJoint = []
    with open('iris.txt') as file:
        for line in file.readlines():
            attributes = line.rstrip().split(',')
            classification = attributes[-1]
            attributes= list(map(float, attributes[:-1]))
            dataFile: data = data(attributes, classification)
            dataJoint.append(dataFile)
    file.close()
    dataTest: newData = newData([7.6, 3, 6.6, 2.1])
    kNeighbord = kNearestNeighbors(3, dataJoint)
    kNeighbord.exec(dataTest)
    print(dataTest.GetClassification())