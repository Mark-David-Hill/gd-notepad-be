from db import db

from models.games import Games

games_list = [
    {
        "name": "Super Mario Bros.",
        "description": "A classic platformer where Mario embarks on a quest to rescue Princess Peach from Bowser.",
        "series": "Mario",
        "genre": "Platformer",
        "image_url": "https://i.ebayimg.com/images/g/eV8AAOSweOhh5i-k/s-l1200.jpg"
    },
    {
        "name": "Super Mario Bros. 3",
        "description": "An iconic platformer that introduces new power-ups and an overworld map.",
        "series": "Mario",
        "genre": "Platformer",
        "image_url": "https://preview.redd.it/title-screen-from-super-mario-bros-3-id-0mdjyp7t-v0-619xejuerjka1.png?width=512&format=png&auto=webp&s=b4c082e51250c2739671f7fd4333f79b8b8c214f"
    },
    {
        "name": "Super Mario World",
        "description": "A groundbreaking platformer with expansive levels and the debut of Yoshi.",
        "series": "Mario",
        "genre": "Platformer",
        "image_url": "https://upload.wikimedia.org/wikipedia/en/3/32/Super_Mario_World_Coverart.png"
    },
    {
        "name": "Super Mario 64",
        "description": "A revolutionary 3D platformer where Mario explores vast, open-world environments in 3D.",
        "series": "Mario",
        "genre": "Platformer",
        "image_url": "https://www.nintendo.com/eu/media/images/10_share_images/games_15/nintendo_7/SI_N64_SuperMario64.jpg"
    },
    {
        "name": "Super Mario Odyssey",
        "description": "A 3D platformer with innovative mechanics, including Mario's new friend Cappy, and vast, diverse worlds.",
        "series": "Mario",
        "genre": "Platformer",
        "image_url": "https://assets.nintendo.com/image/upload/c_fill,w_1200/q_auto:best/f_auto/dpr_2.0/ncom/software/switch/70010000001130/c42553b4fd0312c31e70ec7468c6c9bccd739f340152925b9600631f2d29f8b5"
    }
]

def add_games():
    for index, game in enumerate(games_list):
        if not db.session.query(Games).filter(Games.name == game["name"]).first():

            name = game["name"]
            description = game["description"]
            series = game["series"]
            genre = game["genre"]
            image_url = game["image_url"]
            new_game = Games(name, description, series, genre, image_url)

            db.session.add(new_game)
            
    db.session.commit()

