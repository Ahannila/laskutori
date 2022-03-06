from crypt import methods
from app import app
from flask import redirect, render_template, request, session
import users
import posts
import favourites
import search
import comment

@app.route("/")
def index():
    all_posts = posts.list_posts()
    return render_template("index.html", posts=all_posts)

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
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
            return render_template("login.html", message="Salasana tai käyttäjätunnus väärin")

@app.route("/newpost", methods=["GET", "POST"])
def newpost():
    if request.method == "GET":
        return render_template("newpost.html")
    if request.method == "POST":

        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)

        token = request.form["csrf_token"]
        print(token)
        print(session["csrf_token"])

        title = request.form["title"]
        if len(title) > 20:
            return render_template("newpost.html", message="Otsikko on liian pitkä")
            
        content = request.form["content"]
        if len(content) > 300:
            return render_template("newpost.html", message="Liian pitkä sisältö")

        price = request.form["price"]
        if len(price) > 6:
            return render_template("newpost.html", message="Hinta liian suuri")
        if price == None:
            return render_template("newpost.html", message="Hinta on tyhjä.")

        category = request.form["inputGroupSelect01"]
        if category == "Valitse...":
            return render_template("newpost.html", message="Valitse kategoria")

        if posts.add_post(title,content,price,category):
            return redirect("/")
        else: 
            return render_template("error.html")

@app.route("/del_post", methods=["POST"])
def del_post():
    try:
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        id = request.form["post"]
        favourites.del_favourite_when_deleting_post(id)
        comment.del_comments(id)
        posts.remove_post(id)
        users_posts = posts.get_post_by_creator_id()
        return render_template("userlistings.html", posts=users_posts)
    except:
        return render_template("error.html", error="Jotain meni pieleen poistossa")

@app.route("/favourite", methods=["GET", "POST"])
def favourite():
    if request.method == "GET":
        try:
            faves=favourites.show_favourites()
            return render_template("favourite.html", favourites=faves)
        except:
            return render_template("error.html", error="Kirjaudu sisään nähdäksesi suosikkisi")
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        post = request.form["post"]
        if favourites.add_favourite(post):
            return redirect("/")
        else:
            return render_template("error.html", error="Kohde on jo suosikeissasi")

@app.route("/del_favourite", methods=["POST"])
def del_favourite():
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        try:
            id = request.form["fav_id"] 
            favourites.del_favourite(id)
            faves=favourites.show_favourites()
            return render_template("favourite.html", favourites=faves)
        except: 
            return render_template("error.html", error="Poistossa tapahtui virhe")

@app.route("/post", methods=["POST"])
def post():
    if request.method == "POST":
        id = request.form["id"]
        post = posts.get_post_by_id(id)
        comments = comment.get_comments(id)
        return render_template("post.html", posts=post, comment=comments)

@app.route("/comment", methods=["GET", "POST"])
def comments():
    if request.method == "POST":
        if session["csrf_token"] != request.form["csrf_token"]:
            abort(403)
        post_id = request.form["id"]
        content = request.form["comment"]
        try: 
            comment.add_comment(post_id,content)
            post = posts.get_post_by_id(post_id)
            comments = comment.get_comments(post_id)
            return render_template("post.html", posts=post, comment=comments)
        except: 
            return render_template("error.html", error="tapahtui kommentoitaessa, oletko kirjautunut sisään?")


@app.route("/categories", methods=["GET", "POST"])
def categories():
    return render_template("categories.html")

@app.route("/search")
def query():
    query = request.args["search"]
    print(query)
    result = search.query_results(query)
    return render_template("search.html", result=result)

@app.route("/userlistings")
def user_listings():
    try:
        users_posts = posts.get_post_by_creator_id()
        return render_template("userlistings.html", posts=users_posts)
    except:
        return render_template("error.html", error="Kirjaudu sisään nähdäksesi julkaisusi")

@app.route("/sukset")
def sukset():
    category_posts = posts.get_posts_by_category(1)
    print(category_posts)
    return render_template("kategoriat/sukset.html", posts=category_posts)

@app.route("/laudat")
def laudat():
    category_posts = posts.get_posts_by_category(2)
    return render_template("kategoriat/laudat.html", posts=category_posts)

@app.route("/varusteet")
def varusteet():
    category_posts = posts.get_posts_by_category(3)
    return render_template("kategoriat/varusteet.html", posts=category_posts)