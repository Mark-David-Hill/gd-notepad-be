from db import db

from models.games import Games

games_list = [
    {
        "name": "Super Mario Bros.",
        "description": "A classic platformer where Mario embarks on a quest to rescue Princess Peach from Bowser.",
        "series": "Mario",
        "genre": "Platformer"
    },
    {
        "name": "Super Mario Bros. 3",
        "description": "An iconic platformer that introduces new power-ups and an overworld map.",
        "series": "Mario",
        "genre": "Platformer"
    },
    {
        "name": "Super Mario World",
        "description": "A groundbreaking platformer with expansive levels and the debut of Yoshi.",
        "series": "Mario",
        "genre": "Platformer"
    },
    {
        "name": "Super Mario 64",
        "description": "A revolutionary 3D platformer where Mario explores vast, open-world environments in 3D.",
        "series": "Mario",
        "genre": "Platformer"
    },
    {
        "name": "Super Mario Odyssey",
        "description": "A 3D platformer with innovative mechanics, including Mario's new friend Cappy, and vast, diverse worlds.",
        "series": "Mario",
        "genre": "Platformer"
    }
]

def add_games():
    for index, game in enumerate(games_list):
        if not db.session.query(Games).filter(Games.name == game["name"]).first():

            name = game["name"]
            description = game["description"]
            series = game["series"]
            genre = game["genre"]
            new_game = Games(name, description, series, genre)

            db.session.add(new_game)
            
    db.session.commit()

