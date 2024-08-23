import os

from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

from db import *
from util.blueprints import register_blueprints

database_uri = os.environ.get("DATABASE_URI")
app = Flask(__name__)

CORS(app)

app.config["SQLALCHEMY_DATABASE_URI"] = database_uri
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

init_db(app, db)

register_blueprints(app)

if __name__ == "__main__":
    with app.app_context():
        print("Creating tables...")
        db.create_all()
        print("Tables created successfully")
    app.run(host="127.0.0.1", port='8086')