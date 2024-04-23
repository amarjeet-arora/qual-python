
from flask import Flask,redirect,url_for

app = Flask(__name__)

@app.route("/")
def home():
    return "welcome to flask App"

@app.route("/hello")
def hello():
    return "Hello  to flask App"

@app.route("/admin")
def admin():
    return redirect(url_for("user",name="Amarjeet"))
  

@app.route("/<name>")
def user(name):
    return f"welcome to flask App {name}"

if __name__== "__main__":
    app.run()
