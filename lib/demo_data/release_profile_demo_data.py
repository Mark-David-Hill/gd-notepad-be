from db import db

from models.games import Games

release_profiles = [
    {
        "game_name": "Super Mario Bros.",
        "release_platforms": ["NES"],
        "release_date": "1985-09-13",
        "developer": "Nintendo",
        "publisher": "Nintendo"
    },
    {
        "game_name": "Super Mario Bros. 3",
        "release_platforms": ["NES"],
        "release_date": "1988-10-23",
        "developer": "Nintendo",
        "publisher": "Nintendo"
    },
    {
        "game_name": "Super Mario World",
        "release_platforms": ["SNES"],
        "release_date": "1990-11-21",
        "developer": "Nintendo",
        "publisher": "Nintendo"
    },
    {
        "game_name": "Super Mario 64",
        "release_platforms": ["Nintendo 64"],
        "release_date": "1996-06-23",
        "developer": "Nintendo",
        "publisher": "Nintendo"
    },
    {
        "game_name": "Super Mario Odyssey",
        "release_platforms": ["Nintendo Switch"],
        "release_date": "2017-10-27",
        "developer": "Nintendo",
        "publisher": "Nintendo"
    },
    {
        "game_name": "Mega Man",
        "release_platforms": ["NES"],
        "release_date": "1987-12-17",
        "developer": "Capcom",
        "publisher": "Capcom"
    },
    {
        "game_name": "Mega Man 2",
        "release_platforms": ["NES"],
        "release_date": "1988-12-24",
        "developer": "Capcom",
        "publisher": "Capcom"
    },
    {
        "game_name": "Mega Man 3",
        "release_platforms": ["NES"],
        "release_date": "1990-09-28",
        "developer": "Capcom",
        "publisher": "Capcom"
    },
    {
        "game_name": "Mega Man 4",
        "release_platforms": ["NES"],
        "release_date": "1991-12-06",
        "developer": "Capcom",
        "publisher": "Capcom"
    },
    {
        "game_name": "Mega Man 5",
        "release_platforms": ["NES"],
        "release_date": "1992-12-04",
        "developer": "Capcom",
        "publisher": "Capcom"
    },
    {
        "game_name": "Mega Man 6",
        "release_platforms": ["NES"],
        "release_date": "1993-11-05",
        "developer": "Capcom",
        "publisher": "Capcom"
    },
    {
        "game_name": "Mega Man 7",
        "release_platforms": ["SNES"],
        "release_date": "1995-03-24",
        "developer": "Capcom",
        "publisher": "Capcom"
    },
    {
        "game_name": "Mega Man 8",
        "release_platforms": ["PlayStation", "Sega Saturn"],
        "release_date": "1996-12-17",
        "developer": "Capcom",
        "publisher": "Capcom"
    },
    {
        "game_name": "Mega Man 9",
        "release_platforms": ["Wii", "PlayStation 3", "Xbox 360"],
        "release_date": "2008-09-22",
        "developer": "Inti Creates",
        "publisher": "Capcom"
    },
    {
        "game_name": "Mega Man 10",
        "release_platforms": ["Wii", "PlayStation 3", "Xbox 360"],
        "release_date": "2010-03-01",
        "developer": "Inti Creates",
        "publisher": "Capcom"
    },
    {
        "game_name": "Mega Man 11",
        "release_platforms": ["PlayStation 4", "Xbox One", "Nintendo Switch", "PC"],
        "release_date": "2018-10-02",
        "developer": "Capcom",
        "publisher": "Capcom"
    },
    {
        "game_name": "Mega Man & Bass",
        "release_platforms": ["SNES", "Game Boy Advance"],
        "release_date": "1998-04-24",
        "developer": "Capcom",
        "publisher": "Capcom"
    }
]


# def add_release_profiles():
#     for index, game in enumerate(games_list):
#         if not db.session.query(Games).filter(Games.name == game["name"]).first():

#             name = game["name"]
#             description = game["description"]
#             series = game["series"]
#             genre = game["genre"]
#             image_url = game["image_url"]
#             new_game = Games(name, description, series, genre, image_url)

#             db.session.add(new_game)
            
#     db.session.commit()

