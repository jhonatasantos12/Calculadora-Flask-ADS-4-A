from asyncio.windows_events import NULL
from flask import Flask,render_template, request
 
app = Flask(__name__)

@app.route("/",methods =["POST","GET"])
def calculate():
    resultado =""
    if request.method == "POST":
        n1 =float(request.form.get("n1"))
        n2 =float(request.form.get("n2"))
        op = str(request.form.get("op"))
        if op =="soma":
            resultado = round(n1+n2)
        elif op =="subtracao":
            resultado = round(n1-n2)
        elif op == "divisao":
            resultado =round(n1/n2)
        elif op == "multiplicacao":
            resultado = round(n1*n2)
    if resultado == 0 or resultado == NULL:
        resultado = str(0)
    return render_template("index.html",resultado = resultado)
    
if __name__ == '__main__':
   app.run(debug=True, host='localhost', port=5000)