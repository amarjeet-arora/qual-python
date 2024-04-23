
from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/<name>")
def home2(name):
    return render_template("index.html",mycity=name, myname="amarjeet")

if __name__== "__main__":
    app.run()
