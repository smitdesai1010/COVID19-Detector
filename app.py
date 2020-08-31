from flask import Flask,render_template,request,redirect
import sys
sys.path.append('Model/')
import load_model
from predict import predict

model = load_model.define_model()
app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def get_image():

  if request.method == "POST":
      if not request.files["img"].filename == '':
          image = request.files["img"].read()  
          result = predict(model,image)   

          return render_template('index.html',data = result)
      else:
          return render_template('index.html',data = 'NO FILE SELECTED')


  return render_template('index.html')
  
if __name__ == '__main__':
    app.run(debug = True)  

