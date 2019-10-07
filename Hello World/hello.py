from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World!"

@app.route("/hello")
def harry():
    return "Hello World!"
app.run(debug=True)
