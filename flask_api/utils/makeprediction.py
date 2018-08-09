from sklearn import datasets
from sklearn.neighbors import KNeighborsClassifier
import numpy as np

def predict(inputFeatures):

    iris = datasets.load_iris()

    knn = KNeighborsClassifier()
    knn.fit(iris.data, iris.target)

    inputFeat = np.array(inputFeatures)
    inputFeatures = inputFeat.reshape(1,-1)
    predictInt = knn.predict(inputFeatures)
    if predictInt[0] == 0:
        predictString = 'setosa'
    elif predictInt[0] == 1:
        predictString = 'versicolor'
    elif predictInt[0] == 2:
        predictString = 'virginica'
    else:
        predictString = 'null'

    return predictString

