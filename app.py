
from flask import Flask

# This line creates the Flask app as a global variable
app = Flask(__name__)

# This annotation tells Flask to route any traffic for / to this function
@app.route('/')
def hello():
    return '<h1>Hello World</h1>'


if __name__ == '__main__':
    app.run(port=8000)
