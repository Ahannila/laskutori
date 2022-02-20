from db import db
from flask import session


def query_results(query):
    sql = "SELECT id, title ,content FROM posts WHERE content LIKE :query"
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    results = result.fetchall()
    return results