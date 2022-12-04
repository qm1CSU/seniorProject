from flask import Flask, render_template, request, redirect, url_for
import os 
import csv  

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
def readCPU():  
    with open('data/cpu.csv') as file:  
        data = csv.reader(file, delimiter=',') 
        first_line = True
        cpuData = []
        for row in data: 
            if not first_line: 
                cpuData.append({
                    "product_id": row[0],
                    "product_type": row[1],
                    "product_sku": row[2],
                    "make": row[3],
                    "model": row[4],
                    "price": row[5],
                    "quantity": row[6],
                })     
            else:
                first_line = False
        print(cpuData) 
        return render_template("CPU.html", cpuData=cpuData)

@app.route("/updateCPU", methods=["POST"]) 
def updateCPU():
        cpuData = request.form 
        product_id = cpuData["option1"]
        product_type = cpuData["option2"]
        product_sku = cpuDataa["option3"]  
        make = cpuData["option4"]  
        model = cpuData["option5"]
        price = cpuData["option6"]
        quantity = cpuData["option7"]  
        with open('data/cpu.csv', mode='a') as file:
            cpuData = csv.writer(file, delimiter=',') 
            cpuData.writerow([product_id, product_type, product_sku, make, model, price, quantity])
        print(cpuData)
        return render_template("CPU.html", cpuData=cpuData)       

@app.route("/CPU")                
def CPU():                     
    return render_template("CPU.html")

@app.route("/GPU")
def readGPU():  
    with open('data/gpu.csv') as file:  
        data = csv.reader(file, delimiter=',') 
        first_line = True
        gpuData = []
        for row in data: 
            if not first_line: 
                gpuData.append({
                    "product_id": row[0],
                    "product_type": row[1],
                    "product_sku": row[2],
                    "make": row[3],
                    "model": row[4],
                    "price": row[5],
                    "quantity": row[6],
                })     
            else:
                first_line = False
        print(gpuData) 
        return render_template("GPU.html", gpuData=gpuData)         

@app.route("/GPU") 
def GPU():  
    return render_template("GPU.html") 

@app.route("/ram")  
def readRAM():  
    with open('data/ram.csv') as file:  
        data = csv.reader(file, delimiter=',') 
        first_line = True
        ramData = []
        for row in data: 
            if not first_line: 
                ramData.append({
                    "product_id": row[0],
                    "product_type": row[1],
                    "product_sku": row[2],
                    "make": row[3],
                    "model": row[4],
                    "price": row[5],
                    "quantity": row[6],
                })     
            else:
                first_line = False
        print(ramData) 
        return render_template("ram.html", ramData=ramData) 

@app.route("/ram")                 
def ram():                    
    return render_template("ram.html")

@app.route("/ps") 
def readPS():  
    with open('data/ps.csv') as file:  
        data = csv.reader(file, delimiter=',') 
        first_line = True
        psData = []
        for row in data: 
            if not first_line: 
                psData.append({
                    "product_id": row[0],
                    "product_type": row[1],
                    "product_sku": row[2],
                    "make": row[3],
                    "model": row[4],
                    "price": row[5],
                    "quantity": row[6],
                })     
            else:
                first_line = False
        print(psData) 
        return render_template("ps.html", psData=psData) 

@app.route("/ps")                
def ps():                     
    return render_template("ps.html")
                                        
if __name__== "__main__":
    app.run(debug=True) 