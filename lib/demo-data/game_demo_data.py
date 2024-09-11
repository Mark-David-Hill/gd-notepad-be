from db import db, query

from models.games import Games

games_list = []

def add_games():
    for index, name in enumerate(games_list):
        if not query(Games).filter(Games.name == name).first():

            name = ""

            