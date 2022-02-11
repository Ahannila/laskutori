from sqlalchemy import true
from db import db
import users
from flask import session


def add_favourite(post_id):
    user_id = session["user_id"]
    if user_id == 0:
        return False
    sql = "INSERT INTO favourites (user_id, post_id) VALUES (:user_id, :post_id)"
    db.session.execute(sql, {"user_id":user_id, "post_id":post_id})
    db.session.commit()
    return True

def show_favourites():
    user_id = session["user_id"]
    if user_id == 0:
        return False
    sql = "SELECT P.title, P.content, U.username, P.sent_at, P.price FROM Post P, users U, Favourites F WHERE F.user_id=(:user_id) ORDER BY P.sent_at"
    db.session.execute(sql, {"user_id":user_id})