from keras.models import load_model

def load_Model():
    model_trained = 'static/model_treined/model_06_2023_08_13 23_50_08.h5'
    model_loaded = load_model(model_trained)
    return model_loaded
