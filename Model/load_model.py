import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
from keras.models import load_model
from keras.optimizers import Adam

def define_model():
    model = load_model('Model/saved_model', compile=False)
    model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

    return model   
