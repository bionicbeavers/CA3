from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to calculator Apps"

@app.route('/calc/sub/<int:x>/<int:y>')
def sub(x, y):
    return str(x - y)

@app.route('/calc/mul/<int:x>/<int:y>')
def multiply(x, y):
    return str(x * y)

@app.route('/calc/add/<int:x>/<int:y>')
def add(x, y):
    return str(x + y)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
