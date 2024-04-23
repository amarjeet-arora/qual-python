
from flask import Flask,redirect,url_for,render_template

app = Flask(__name__)

userdata=['admin','manager','qa']

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/login")
def login():
    return render_template("login.html")

@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/<name>")
def home2(name):
    return render_template("index.html",users=userdata)

if __name__== "__main__":
    app.run(debug=True)






{% extends "base.html"%}

{% block title %} Login Page {% endblock %}


{% block content %} <h2>User Login</h2>{% endblock %}





{% extends "base.html"%}

{% block title %} register Page {% endblock %}


{% block content %} <h2>Registration App</h2>{% endblock %}





<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{% block title %} {% endblock %}</title>
</head>
<body>
    <h1>Amarjeets Website</h1>
    {% block content %}
     {% endblock %}
</body>
</html>
