from sqlalchemy import true
from db import db
import users
from flask import session


def add_favourite(post_id):
    user_id = session["user_id"]
    if user_id == 0:
        return False
    if already_favourite(post_id):
        return False
    sql = "INSERT INTO favourites (user_id, post_id) VALUES (:user_id, :post_id)"
    db.session.execute(sql, {"user_id":user_id, "post_id":post_id})
    db.session.commit()
    return True

def show_favourites():
    user_id = session["user_id"]
    if user_id == 0:
        return False
    sql = "SELECT P.title, P.content, F.post_id, U.username FROM Post P, Favourites F, users U WHERE F.user_id=(:user_id) AND P.id=F.post_id AND P.creator_id=U.id;"
    result = db.session.execute(sql, {"user_id":user_id})
    return result.fetchall()

def already_favourite(post_id):
    user_id = session["user_id"]
    sql = "SELECT post_id FROM Favourites WHERE user_id=(:user_id) and post_id=(:post_id)"
    result = db.session.execute(sql, {"user_id":user_id, "post_id":post_id})
    comp = result.fetchone()

    if comp:
        return True
    else:
        False

def del_favourite(id):
    user_id = session["user_id"]
    sql = "DELETE FROM Favourites WHERE post_id=(:id) AND user_id=(:user_id)"
    db.session.execute(sql,{"user_id":user_id,"id":id})
    res = db.session.commit()
    if res:
        return True
    else:
        False

def del_favourite_when_deleting_post(id):
    sql = "DELETE FROM Favourites WHERE post_id=(:id)"
    db.session.execute(sql,{"id":id})
    db.session.commit()
    return True