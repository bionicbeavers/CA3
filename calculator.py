from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to calculator App"

@app.route('/sub/<int:x>/<int:y>')
def sub(x, y):
    return (x - y)
  
@app.route('/calc/mul/<int:x>/<int:y>')
def multiply(x, y):
    return (x * y)

@app.route('/calc/add/<int:x>/<int:y>')
def add(x, y):
    return (x + y)

if __name__ == '__main__':
    app.run()