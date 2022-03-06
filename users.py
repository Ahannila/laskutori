from db import db
from flask import session
import secrets
from werkzeug.security import check_password_hash, generate_password_hash

def register(username, password):
    hash_value = generate_password_hash(password)

    print("Kokeillaan rekisteröidä")
    sql = "INSERT INTO users (username,password) VALUES (:username, :password)"
    db.session.execute(sql, {"username":username, "password":hash_value})
    db.session.commit()

    return login(username, password)

def login(username, password):
    sql = "SELECT id, password FROM users WHERE username=:username"
    result = db.session.execute(sql, {"username":username})
    user = result.fetchone()
    if not user:
        return False
    else:
        if check_password_hash(user.password, password):
            session["user_id"] = user.id
            session["csrf_token"] = secrets.token_hex(16)
            return True
        else:
            return False

def logout():
    del session["user_id"]

def user_id():
    return session["user_id",0]