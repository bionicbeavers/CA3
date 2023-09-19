from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to calculator App"

@app.route('/sub/<int:x>/<int:y>')
def sub(x, y):
    return str(x - y)

if __name__ == '__main__':
    app.run()