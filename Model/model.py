from keras.models import load_model
from keras.optimizers import Adam
from tensorflow import expand_dims
import cv2
import numpy as np

def define_model():
    model = load_model('saved_model/', compile=False)
    model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

    return model   

def predict(model):
    img = cv2.imread('normal-1.jpg' , cv2.IMREAD_COLOR)
    try:
        img = cv2.resize(img, (256,256))

    except:
        print('error')

    img = np.array(img)
    img = expand_dims(img,0)    
    list = model.predict(img)
    #print(type(list))

    return np.argmax(list)

if __name__ == '__main__':
     model = define_model()
     index = predict(model)

     predictions = ['covid-19','normal','pnuemonia']   
     #print(index,type(index))  
     print(predictions[index])