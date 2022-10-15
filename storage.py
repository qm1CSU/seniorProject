from flask import Flask, render_template, request
import os           
app = Flask(__name__)

IMG_FOLDER = os.path.join('static', 'pics')

app.config['UPLOAD_FOLDER'] = IMG_FOLDER



@app.route("/")
def Display_IMG():
     storage = os.path.join(app.config['UPLOAD_FOLDER'], 'storage.jpg')
     return render_template("homepage.html", user_image=storage)



@app.route("/")                
def home():                    
    return render_template("homepage.html")

@app.route("/CPU")
def Show_IMG():
     ryzen = os.path.join(app.config['UPLOAD_FOLDER'], 'ryzen.jpg')
     return render_template("CPU.html", user_image=ryzen)


@app.route("/CPU")                
def CPU():                    
    return render_template("CPU.html")

                                           
    
if __name__== "__main__":
    app.run(debug=True)
