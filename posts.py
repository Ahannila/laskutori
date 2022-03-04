from sqlalchemy import true
from db import db
import users
from flask import session


def add_post(title, content, price, category_id):
    creator_id = session["user_id"]
    if creator_id == 0:
        return False
    sql = "INSERT INTO Post (title,content,price,creator_id,sent_at, category_id) VALUES (:title, :content, :price, :creator_id, NOW(),:category_id)"
    db.session.execute(sql, {"title":title,"content":content, "price":price, "creator_id":creator_id, "category_id":category_id})
    db.session.commit()
    return True

def list_posts():
    sql = "SELECT P.title, P.content, U.username, P.sent_at, P.price, P.id FROM Post P, users U WHERE P.creator_id=U.id ORDER BY P.sent_at"
    result = db.session.execute(sql)
    return result.fetchall()  

def get_posts_by_category(category_id):
    sql = "SELECT P.title FROM post P LEFT JOIN category C ON C.id = P.category_id WHERE C.id = (:id)  ORDER BY C.id;"
    result = db.session.execute(sql,{"id":category_id})
    return result.fetchall() 

def get_post_by_id(id):
    sql = "SELECT P.title, P.content, P.id FROM Post P WHERE P.id=(:id);"
    result = db.session.execute(sql,{"id":id})
    return result.fetchall()

def get_post_by_creator_id():
    id = session["user_id"]
    if id == 0:
        return False
    sql = "SELECT P.title, P.content, P.id, P.sent_at FROM Post P WHERE P.creator_id=(:id);"
    result = db.session.execute(sql,{"id":id})
    return result.fetchall()

def remove_post(id):
    sql = "DELETE FROM post WHERE id=(:id)"
    db.session.execute(sql,{"id":id})
    result = db.session.commit()
    if result:
        return True
    else:
        return False



