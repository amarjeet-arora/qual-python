
from flask import Flask,redirect,url_for,render_template,request

app = Flask(__name__)

userdata=['admin','manager','qa']

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        user=request.form["nm"]
        return redirect(url_for("home2",usr=user))
    else:
        return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")







{% extends "base.html"%}

{% block title %} Login Page {% endblock %}


{% block content %} <h2>User Login</h2>
<hr>

<form method="post" action="#">
    UserName: <input type="text" name="nm"/>
    <button>Login</button>
</form>

{% endblock %}

@app.route("/<usr>")
def home2(usr):
    #return render_template("userdata.html")
    return f"<h3>{usr}</h3>"

if __name__== "__main__":
    app.run(debug=True)
