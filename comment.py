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
    sql = "SELECT comment, user_id, sent_at FROM comments WHERE post_id=(:post_id)"
    result = db.session.execute(sql,{"post_id":id})
    return result.fetchall()