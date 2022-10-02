  
from flask import Flask , redirect, url_for, request, render_template, jsonify
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("input.html")

@app.route('/answer', methods = ["POST"])
def asd():
    num1 = request.form['num1']
    num2 = request.form['num2']
    
    return render_template("answer.html", answer = int(num1) + int(num2))

if __name__ == '__main__':
    app.run( port=80, debug= True, host='0.0.0.0')
