from flask import Flask,render_template,request,redirect

app = Flask(__name__)

@app.route('/', methods=["GET","POST"])
def get_image():
  if request.method == "POST":
      if request.files:
          image = request.files["img"]
          print(image)

          return redirect(request.url)

  return render_template('index.html')
  
if __name__ == '__main__':
    app.run(debug = True)  