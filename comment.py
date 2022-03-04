from db import db
from flask import session

def add_comment(id,content):
    creator_id = session["user_id"]
    if creator_id == None:
        return False
    sql = "INSERT INTO comments(post_id, user_id, comment, sent_at) VALUES (:post_id, :user_id, :content, NOW())"
    db.session.execute(sql,{"post_id":id, "user_id":creator_id, "content":content})
    db.session.commit()
    return True

def get_comments(id):
    sql = "SELECT C.comment, C.user_id, C.sent_at, U.username FROM comments C, users U WHERE U.id=C.user_id AND post_id=(:post_id)"
    result = db.session.execute(sql,{"post_id":id})
    return result.fetchall()

def del_comments(post_id):
    sql = "DELETE FROM comments where post_id=(:post_id)"
    db.session.execute(sql,{"post_id":post_id})
    db.session.commit()
    return True