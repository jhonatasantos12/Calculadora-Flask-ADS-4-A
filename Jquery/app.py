
from flask import Flask, jsonify,render_template, request
 
app = Flask(__name__)

@app.route("/index",methods =["GET"])
def index():
    return render_template("index.html")
    

@app.route("/api/retorno",methods =["post"])
def api():
    json = request.get_json()
    a = json['first_name']
    a = a.lower()
    b =json['second_name']
    b = b.lower()
    json['first_name'] = a 
    json['second_name'] = b 
    json['Completo'] = json['first_name']+ json['second_name']
    return jsonify(json)
    
if __name__ == '__main__':
   app.run(debug=True, host='localhost', port=5000)