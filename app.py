from flask import Flask
import os

app = Flask(__name__)


@app.route("/",methods=['GET'])
def hello_world():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)