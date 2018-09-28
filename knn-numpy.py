import numpy as np
import pandas as pd

from scipy import stats


from statistics import mode

def mainFunction():
    trainingSet,testSet=read_file_into_array()
    classified_items=classify(trainingSet,testSet)
    accuracy=computeAccuracy(classified_items)
    print(classified_items)
    print(accuracy)

def classify(testSet,trainingSet):
    classifiedSet=[]
    for i in range(0, testSet.shape[0]):
        classifiedSet.append(classifyInstances(trainingSet,testSet[i]))
    print(classifiedSet)
    return classifiedSet

def classifyInstances(trainingSet, testSet_instance):
    distances = []
    for i in range(0, trainingSet.shape[0]):
        dist = computeDistance(trainingSet[i], testSet_instance)
        distances.append([trainingSet[i,4], dist,])
        nd_dist=np.array(distances)
    nd_dist.view('i8,i8').sort(order=['f1'], axis=0)
    neignbours=nd_dist[:3,0]
    classisied_as=int(mode(list(neignbours)))
    classifiedInstance=np.append(testSet_instance,classisied_as)
    # print(classifiedInstance)
    return classifiedInstance

def read_file_into_array():
    df = pd.read_csv('IRIS.csv')
    divider = int(len(df) * 0.64)
    x,y= np.split(df, [int(.34 * len(df))])
    testSet =x.values
    trainingSet = y.values
    return trainingSet,testSet

def computeDistance(vector1, vector2):
    return np.sqrt(np.sum(np.power(vector1-vector2, 2)))

def computeAccuracy(testset):
     counter=0
     for x in testset:
         if x[4]==x[5]:
             counter+=1
     accuracy=round((counter/len(testset))*100,2)
     return accuracy
mainFunction()








































# %matplotlib inline
    # =====================================================================
# def read_csv_pandas():
#      df= pd.read_csv('IRIS.csv')
#      x,y= np.split(df, [int(.34 * len(df))])
#      trainingSet=x.values
#      testSet=y.values
#
#
# def euclidean_distance(vector1, vector2):
#     return np.sqrt(np.sum(np.power(vector1-vector2, 2)))
#
#
# def get_neighbours(X_train, X_test_instance, k):
#     distances = []
#     neighbors = []
#     for i in range(0, X_train.shape[0]):
#         dist = euclidean_distance(X_train[i], X_test_instance)
#         distances.append((i, dist))
#     distances.sort(key=operator.itemgetter(1))
#     for x in range(k):
#         #print distances[x]
#         neighbors.append(distances[x][0])
#     return neighbors
#
# def predictkNNClass(output, y_train):
#     classVotes = {}
#     for i in range(len(output)):
# #         print output[i], y_train[output[i]]
#         if y_train[output[i]] in classVotes:
#             classVotes[y_train[output[i]]] += 1
#         else:
#             classVotes[y_train[output[i]]] = 1
#     sortedVotes = sorted(classVotes.iteritems(), key=operator.itemgetter(1), reverse=True)
#     #print sortedVotesdef kNN_test(X_train, X_test, Y_train, Y_test, k):
#     output_classes = []
#     for i in range(0, X_test.shape[0]):
#         output = get_neighbours(X_train, X_test[i], k)
#         predictedClass = predictkNNClass(output, Y_train)
#         output_classes.append(predictedClass)
#     return output_classes
#
# def kNN_test(X_train, X_test, Y_train, Y_test, k):
#         output_classes = []
#         for i in range(0, X_test.shape[0]):
#             output = get_neighbours(X_train, X_test[i], k)
#             predictedClass = predictkNNClass(output, Y_train)
#             output_classes.append(predictedClass)
#         return output_classes
#
#
#
#
#     return sortedVotes[0][0]
#
# #
