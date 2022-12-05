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

@app.route("/updateCPU", methods=['POST'])  
def updateCPU(): 
        product_id = request.form['product_id']
        product_type = request.form['product_type']
        product_sku = request.form['product_sku']  
        make = request.form['make'] 
        model = request.form['model']
        price = request.form['price']
        quantity = request.form['quantity'] 
        with open('data/cpu.csv') as file:
            data = csv.writer(file, delimiter=',') 
        for row in data:  
            cpuData.append({
                "product_id": row[0],
                "product_type": row[1],
                "product_sku": row[2],
                "make": row[3],
                "model": row[4],
                "price": row[5],
                "quantity": row[6],
            })
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

@app.route("/updateGPU", methods=["POST"]) 
def updateGPU():
        request.method == "POST"
        gpuData = dict(request.form)  
        product_id = gpuData["product_id"] [0]
        product_type = gpuData["product_type"] [0]
        product_sku = gpuDataa["product_sku"] [0]  
        make = gpuData["make"] [0]  
        model = gpuData["model"] [0]
        price = gpuData["price"] [0]
        quantity = gpuData["quantity"] [0]  
        with open('data/gpu.csv', mode='a') as file:
            gpuData = csv.writer(file, delimiter=',') 
            gpuData.writerow([product_id, product_type, product_sku, make, model, price, quantity])
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

@app.route("/updateRAM", methods=["POST"]) 
def updateRAM():
        request.method == "POST"
        ramData = dict(request.form) 
        product_id = ramData["product_id"] [0]
        product_type = ramData["product_type"] [0]
        product_sku = ramDataa["product_sku"] [0]  
        make = ramData["make"] [0]  
        model = ramData["model"] [0]
        price = ramData["price"] [0]
        quantity = ramData["quantity"] [0]    
        with open('data/ram.csv', mode='a') as file:
            ramData = csv.writer(file, delimiter=',') 
            ramData.writerow([product_id, product_type, product_sku, make, model, price, quantity])
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

@app.route("/updatePS", methods=["POST"]) 
def updatePS(): 
        request.method == "POST" 
        psData = dict(request.form) 
        product_id = psData["product_id"] [0]
        product_type = psData["product_type"] [0]
        product_sku = psData["product_sku"] [0]  
        make = psData["make"] [0]  
        model = psData["model"] [0]
        price = psData["price"] [0]
        quantity = psData["quantity"] [0]
        with open('data/ps.csv', mode='a') as file:
            psData = csv.writer(file, delimiter=',') 
            psData.writerow([product_id, product_type, product_sku, make, model, price, quantity])
        print(psData)
        return render_template("ps.html", psData=psData)

@app.route("/ps")                
def ps():                     
    return render_template("ps.html")
                                        
if __name__== "__main__":
    app.run(debug=True) 