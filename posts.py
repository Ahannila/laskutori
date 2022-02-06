from db import db


def add_post():
    sql = "INSERT INTO posts (content,user_id,sent_at) VALUES (:content, :user_id, NOW())"
    return 