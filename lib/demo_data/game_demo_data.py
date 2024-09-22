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
    },
    {
        "name": "Mega Man",
        "description": "The original Mega Man game, introducing the series' signature gameplay and six Robot Masters.",
        "series": "Mega Man",
        "genre": "Action/Platformer",
        "image_url": ""
    },
    {
        "name": "Mega Man 2",
        "description": "The second game in the series, widely regarded as one of the best, featuring eight Robot Masters and refined gameplay.",
        "series": "Mega Man",
        "genre": "Action/Platformer",
        "image_url": ""
    },
    {
        "name": "Mega Man 3",
        "description": "The third entry in the series, introducing the slide mechanic and Proto Man.",
        "series": "Mega Man",
        "genre": "Action/Platformer",
        "image_url": ""
    },
    {
        "name": "Mega Man 4",
        "description": "Mega Man's fourth adventure, which introduces the charge shot ability.",
        "series": "Mega Man",
        "genre": "Action/Platformer",
        "image_url": ""
    },
    {
        "name": "Mega Man 5",
        "description": "The fifth installment, with new gameplay tweaks and eight new Robot Masters.",
        "series": "Mega Man",
        "genre": "Action/Platformer",
        "image_url": ""
    },
    {
        "name": "Mega Man 6",
        "description": "The sixth entry, which was the last Mega Man game for the NES, featuring Rush Adaptors for more versatile gameplay.",
        "series": "Mega Man",
        "genre": "Action/Platformer",
        "image_url": ""
    },
    {
        "name": "Mega Man 7",
        "description": "The first Mega Man game for the Super NES, featuring more detailed sprites and a storyline involving Bass and Treble.",
        "series": "Mega Man",
        "genre": "Action/Platformer",
        "image_url": ""
    },
    {
        "name": "Mega Man 8",
        "description": "The first and only Mega Man game on the original PlayStation, featuring 2.5D graphics and eight Robot Masters.",
        "series": "Mega Man",
        "genre": "Action/Platformer",
        "image_url": ""
    },
    {
        "name": "Mega Man 9",
        "description": "The ninth entry returns to 8-bit graphics and mechanics, bringing back the classic NES-style gameplay.",
        "series": "Mega Man",
        "genre": "Action/Platformer",
        "image_url": ""
    },
    {
        "name": "Mega Man 10",
        "description": "The tenth game, also in 8-bit style, featuring a harder difficulty mode and extra playable characters.",
        "series": "Mega Man",
        "genre": "Action/Platformer",
        "image_url": ""
    },
    {
        "name": "Mega Man 11",
        "description": "The latest entry in the series, featuring a 2.5D style, the Double Gear system, and vibrant graphics.",
        "series": "Mega Man",
        "genre": "Action/Platformer",
        "image_url": ""
    },
    {
        "name": "Mega Man & Bass",
        "description": "A spin-off game that allows players to choose between Mega Man and Bass, with different abilities for each character.",
        "series": "Mega Man",
        "genre": "Action/Platformer",
        "image_url": ""
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

