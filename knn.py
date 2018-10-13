

import csv
from statistics import mode

from math import sqrt
import copy



def mainFunction():
    trainingSet,testSet=read_file_into_array()
    classified_items = Classify_items(testSet, trainingSet)
    accuracy=computeAccuracy(classified_items)
    print(classified_items)
    print('accuracy=',accuracy)


def read_file_into_array():
    testSet=[]
    testSet=[]
    with open('IRIS.csv', newline='') as csvfile:
         data = list(csv.reader(csvfile))
         divider=int(len(data)*0.66)
         testSet=data[:divider]
         trainingSet=data[divider:]
    return trainingSet,testSet

def Classify_items(testSet,trainingSet):
         # loop through training set classifying each data
         for index,testItem in enumerate(testSet):
             workingTrainingSet=copy.deepcopy(trainingSet)
             for trainingItem in workingTrainingSet:
                 distance=defcomputeDistance(testItem,trainingItem)
                 trainingItem.append(distance);
             sortedList=sorted(workingTrainingSet,key=lambda x:x[5])
             first3=sortedList[:3]
             clasification=mode([first3[0][4],first3[1][4],first3[2][4]])
             testItem.append(clasification)
         return testSet

def defcomputeDistance(x,y):
    distance =sqrt((float(x[0])-float(y[0]))**2 + (float(x[1])-float(y[1]))**2 + (float(x[2])-float(y[2]))**2 + (float(x[3])-float(y[3]))**2)
    return distance

def computeAccuracy(testset):
     counter=0
     for x in testset:
         if x[4]==x[5]:
             counter+=1
     accuracy=round((counter/len(testset))*100,2)
     return accuracy

mainFunction()
