from db import db
from flask import session


def query_results(query):
    sql = "SELECT id, title ,content FROM post WHERE title LIKE :query"
    result = db.session.execute(sql, {"query":"%"+query+"%"})
    results = result.fetchall()
    print(results)
    return results