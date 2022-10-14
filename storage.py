@app.route("/")
def Display_IMG():
     storage = os.path.join(app.config['UPLOAD_FOLDER'], 'storage.jpg')
     return render_template("homepage.html", user_image=storage)



@app.route("/")                
def home():                    
    return render_template("homepage.html")


                                           
    
if __name__== "__main__":
    app.run(debug=True)
