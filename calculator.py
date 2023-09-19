from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to calculator App"

@app.route('/calc/mul/<int:x>/<int:y>')
def mul(x, y):
    return str(x * y)

if __name__ == '__main__':
    app.run()