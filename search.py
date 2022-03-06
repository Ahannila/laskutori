from db import db
from flask import session


def query_results(query):
    sql = "SELECT P.title, P.content, U.username, P.sent_at, P.price, P.id FROM Post P, users U WHERE P.creator_id=U.id AND title LIKE :query"
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    results = result.fetchall()
    return results