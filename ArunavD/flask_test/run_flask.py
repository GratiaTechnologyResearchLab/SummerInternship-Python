from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
   return "Hello World!"
@app.route("/home")
def new():
    return "I am god"