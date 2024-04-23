
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





<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8" />
    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Document</title>
  </head>
  <body>
    Welcome to Flask!!!!! {{mycity}} -- {{myname}}

    <hr />
    {% for x in range(10) %} {% if x%2 ==1 %}

    <p>{{x}}</p>
    {% endif %} {% endfor %}
  </body>
</html>
