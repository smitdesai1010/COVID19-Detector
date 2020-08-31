import cv2
import numpy as np


def predict(model,image):
    img = cv2.imdecode(np.fromstring(image,np.uint8),cv2.IMREAD_COLOR)
    try:
        img = cv2.resize(img, (256,256))

    except:
        print('error')

    img = np.array(img)
    img = np.expand_dims(img,axis=0)    
    list = model.predict(img)
    index  = np.argmax(list)

    predictions = ['covid-19','normal','pnuemonia']   

    return predictions[index]

