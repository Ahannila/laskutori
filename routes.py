from email import message
from app import app
from flask import redirect, render_template, request
import users

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        print("Routes GET")
        return render_template("register.html")
    if request.method == "POST":
        print("routes POST")
        username = request.form["username"]
        password = request.form["password"]
        if users.register(username, password):
            return redirect("/")
        else: 
            return render_template("error.html")