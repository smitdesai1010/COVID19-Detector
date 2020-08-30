from keras.models import load_model

model = load_model('saved_model/', compile=False)
model.summary()

model('covid19-1.jpg')