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
      if request.files:
          image = request.files["img"].read()  
          print(predict(model,image))   

          return redirect(request.url)

  return render_template('index.html')
  
if __name__ == '__main__':
    app.run(debug = True)  

