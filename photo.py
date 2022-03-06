from db import db
from flask import session



def upload_photo(file, name):
    if not name.endswith(".jpg"):
        return "Invalid filename"
    data = file.read()
    if len(data) > 100*1024:
        return "Too big file"
    sql = "INSERT INTO images (name,data) VALUES (:name,:data)"
    db.session.execute(sql, {"name":name, "data":data})
    db.session.commit()
    return True

