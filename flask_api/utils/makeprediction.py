
import numpy as np
def predict(inputFeatures):
    from keras.models import model_from_json
    from keras import backend as K

    # Needed to clear all the variables
    K.clear_session()
    
    # load json file and create model
    json_file = open( 'model.json' , 'r' )
    loaded_model_json = json_file.read()
    json_file.close()
    loaded_model = model_from_json(loaded_model_json)
    # load weights into new model
    loaded_model.load_weights("model.h5")

    # Transform inputFeatures
    inputFeatures = np.array([inputFeatures])

    # Predict
    prediction = loaded_model.predict(inputFeatures)

    # Get the winning index
    predictInt = np.argmax(prediction)
    
    if predictInt == 0:
        predictString = 'Nothing in hand; not a recognized poker hand'
    elif predictInt == 1:
        predictString = 'One pair; one pair of equal ranks within five cards'
    elif predictInt == 2:
        predictString = 'Two pairs; two pairs of equal ranks within five cards'
    elif predictInt == 3:
        predictString = 'Three of a kind; three equal ranks within five cards'
    elif predictInt == 4:
        predictString = 'Straight; five cards sequentially ranked with no gaps'
    elif predictInt == 5:
        predictString = 'Flush; five cards with the same suit'
    elif predictInt == 6:
        predictString = 'Full house; pair + different rank three of a kind'
    elif predictInt == 7:
        predictString = 'Four of a kind; four equal ranks within five cards'
    elif predictInt == 8:
        predictString = 'Straight flush; straight + flush'
    elif predictInt == 9:
        predictString = 'Royal flush; {Ace, King, Queen, Jack, Ten} + flush'
    else:
        predictString = 'null'

    return predictString

