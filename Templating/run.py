from flask import Flask, render_template
app = Flask(__name__)

@app.route("/static")
def hello():
    return render_template('static.html')

@app.route("/dynamic")
def harry():
    name = "Sandeep"
    return render_template('dynamic.html', name2= name)
app.run(debug=True)