# Load libraries
from pandas import read_csv
from pandas.plotting import scatter_matrix
#from matplotlib import pyplot
#from sklearn.model_selection import train_test_split
from sklearn.model_selection import KFold
from sklearn.model_selection import cross_val_score
from sklearn.metrics import classification_report
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from xgboost import XGBClassifier
from keras.models import Sequential
from keras.layers import Dense
from keras.utils import to_categorical
from keras.models import model_from_json
import numpy as np
# Load dataset
names = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'class']
testData = read_csv('poker-hand-testing.data',names=names)
trainData = read_csv('poker-hand-training-true.data')
print(testData.shape)

X_train = trainData.values[:,0:-1]
Y_train = trainData.values[:,-1]
X_test = testData.values[:,0:-1]
Y_test = testData.values[:,-1]

# shape of dataset
print(testData.shape)

# see first rows of the data
print(testData.describe())
#names = [ sepangth , sepal-width , petal-length ,
#dataset = read_csv(filename, names=names)

# class distribution
print(testData.groupby( 'class' ).size())

# check models
models = []
models.append(( 'LDA' , LinearDiscriminantAnalysis()))
models.append(( 'KNN' , KNeighborsClassifier()))
models.append(( 'CART' , DecisionTreeClassifier()))
models.append(( 'XGB' , XGBClassifier(n_estimators=100,max_depth=3,learning_rate=0.8)))
# evaluate models
results = []
names = []
seed = 5 

for name, model in models:
    kfold = KFold(n_splits=5, random_state=seed)
    cv_results = cross_val_score(model, X_train, Y_train, cv=kfold, scoring= 'accuracy' )
    results.append(cv_results)
    names.append(name)
    msg = "%s: %f (%f)" % (name, cv_results.mean(), cv_results.std())
    print(msg)
# transform labels to categorical
y_test = to_categorical(Y_test)
y_train = to_categorical(Y_train)
# create a neural network
model = Sequential()
model.add(Dense(85, input_dim=10, activation= 'relu' ))
model.add(Dense(120,activation ='tanh'))
model.add(Dense(80, activation= 'relu' ))
model.add(Dense(40, activation= 'relu' ))
model.add(Dense(10, activation= 'softmax' ))
# Compile the network
model.compile(loss= 'categorical_crossentropy' , optimizer= 'adam' , metrics=[ 'accuracy' ])
# Fit the network
model.fit(X_train, y_train, epochs=50, batch_size=50)#,verbose=1,validation_data=(X_test,y_test))
# evaluate
scores = model.evaluate(X_test, y_test)
print(scores[1])

# serialize model to JSON
#model_json = model.to_json()
#with open("model.json", "w") as json_file:
 #   json_file.write(model_json)
# serialize weights to HDF5
#model.save_weights("model.h5")
#print("Saved model to disk")


 # load json file and create model
json_file = open( 'model.json' , 'r' )
loaded_model_json = json_file.read()

json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")
inputFeatures = [1,2,1,3,1,4,1,5,1,6]
print(inputFeatures)
    
features = np.array(inputFeatures)
inputFeatures = features.reshape(1,-1)
print(inputFeatures)
#loaded_model.compile(loss= 'binary_crossentropy' , optimizer= 'adam' , metrics=[ 'accuracy' ])
prediction = loaded_model.predict(inputFeatures)
ans = np.argmax(prediction)
print(prediction)
print(ans)
print(np.sum(prediction))

