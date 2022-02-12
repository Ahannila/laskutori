from calendar import c
from crypt import methods
from app import app
from flask import redirect, render_template, request, session
import users
import posts
import favourites

@app.route("/")
def index():
    all_posts = posts.list_posts()
    return render_template("index.html", posts=all_posts)

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

@app.route("/logout")
def logout():
    users.logout()
    return redirect("/")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]
        if users.login(username, password):
            return redirect("/")
        else:
            return render_template("error.html")

@app.route("/newpost", methods=["GET", "POST"])
def newpost():
    if request.method == "GET":
        return render_template("newpost.html")
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        price = request.form["price"]
        if posts.add_post(title,content,price):
            return redirect("/")
        else: 
            return render_template("error.html")

@app.route("/favourite", methods=["GET", "POST"])
def favourite():
    if request.method == "GET":
        faves=favourites.show_favourites()
      
        return render_template("favourite.html", favourites=faves)
    if request.method == "POST":
        post = request.form["post"]
        if favourites.add_favourite(post):
            return redirect("/")
