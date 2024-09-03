from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_route():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return str(add(a, b))

@app.route('/sub')
def sub_route():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return str(sub(a, b))

@app.route('/mult')
def mult_route():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return str(mult(a, b))

@app.route('/div')
def div_route():
    a = float(request.args.get('a', 0))
    b = float(request.args.get('b', 0))
    return str(div(a, b))

if __name__ == '__main__':
    app.run(debug=True)

