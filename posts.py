from sqlalchemy import true
from db import db
import users
from flask import session


def add_post(title, content, price):
    creator_id = session["user_id"]
    if creator_id == 0:
        return False
    sql = "INSERT INTO Post (title,content,price,creator_id,sent_at) VALUES (:title, :content, :price, :creator_id, NOW())"
    db.session.execute(sql, {"title":title,"content":content, "price":price, "creator_id":creator_id})
    db.session.commit()
    return True

def list_posts():
    sql = "SELECT P.title, P.content, U.username, P.sent_at, P.price, P.id FROM Post P, users U WHERE P.creator_id=U.id ORDER BY P.sent_at"
    result = db.session.execute(sql)
    return result.fetchall()   

def remove_post():
    sql = "DELETE FROM post WHERE creator_id VALUES (:creator_id)"