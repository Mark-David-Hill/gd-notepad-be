from flask_bcrypt import generate_password_hash

from db import db
from models.app_users import AppUsers

users_list = [
    {
        "first_name": "Super",
        "last_name": "Admin",
        "email": "super@test.com",
        "role": "super-admin"
    },
    {
        "first_name": "Admin",
        "last_name": "User",
        "email": "admin@test.com",
        "role": "admin"
    },
    {
        "first_name": "Standard",
        "last_name": "User",
        "email": "user@test.com",
        "role": "user"
    },
]

def add_users():
    for index, user in enumerate(users_list):
        if not db.session.query(AppUsers).filter(AppUsers.email == user["email"]).first():

            first_name = user["first_name"]
            last_name = user["last_name"]
            email = user["email"]
            password = generate_password_hash("1234").decode('utf8')
            role = user["role"]
            new_user = AppUsers(first_name, last_name, email, password, role)

            db.session.add(new_user)
            db.session.commit()