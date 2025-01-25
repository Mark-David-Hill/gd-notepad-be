from db import db

from models.collections import Collections
from models.types import Types


smb_types_list = [
    {"name": "Mechanic", "image_url": "https://www.pngall.com/wp-content/uploads/5/Game-Controller-PNG-Clipart.png", "color": "#0007d1"}, 
    {"name": "Level", "image_url": "https://www.shutterstock.com/image-vector/2d-arcade-game-level-cartoon-260nw-2259956823.jpg", "color": "#d15e00"},
    {"name": "Level Element", "image_url": "https://i.pinimg.com/564x/6e/e9/b5/6ee9b5fdd1f67fbac5fd80445be55245.jpg", "color": "#f26d00"},
    {"name": "Enemy Element", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyFefeRiOb3lbMSFGyX6SGFnRD39v7GOr-mg&s", "color": "#e60400"},
    {"name": "Power Up", "image_url": "https://static.vecteezy.com/system/resources/previews/026/973/044/non_2x/3d-icon-video-games-rendered-isolated-on-the-transparent-background-power-up-icon-for-your-design-png.png", "color": "#13e600"}
]

wd_types_list = [
    {"name": "Book", "image_url": "https://i.pinimg.com/474x/d4/d3/c0/d4d3c02f855019b7357b6c46da2124da.jpg"},
    {"name": "Part", "image_url": "https://banner2.cleanpng.com/20180314/ikq/av0d580el.webp"},
    {"name": "Chapter", "image_url": "https://lessonpix.com/drawings/143374/380x380/Chapter.png"},
    {"name": "Character", "image_url": "https://t3.ftcdn.net/jpg/01/41/00/42/360_F_141004267_gvTQBCsccv1t6oSwtLG9CmzJY0mXzqeV.jpg"},
    {"name": "Location", "image_url": "https://png.pngtree.com/png-vector/20220914/ourmid/pngtree-natural-green-hills-transparent-clipart-png-image_6174296.png"},
    {"name": "Species", "image_url": "https://www.creativefabrica.com/wp-content/uploads/2021/12/21/1640087346/Farm-Animal-Silhouettes-black-version-580x386.jpg"},
    {"name": "Character Group", "image_url": "https://img.freepik.com/premium-vector/set-rabbits-silhouette-drawing-white-black_1263357-4739.jpg"},
    {"name": "Time", "image_url": "https://media.istockphoto.com/id/964947830/vector/calendar.jpg?s=612x612&w=0&k=20&c=O8oeRZpK_gTshy-acC0PkRZSrih9KXULv7ZNfLwCyHU="},
]

chinese_characters_types_list = [
    {"name": "Chinese Character", "image_url": ""},
    {"name": "Radical", "image_url": ""},
    {"name": "Meaning", "image_url": ""},
    {"name": "Pronunciation", "image_url": ""},
    {"name": "Character Set", "image_url": ""}
]

programming_technology_types_list = [
    {"name": "Language", "image_url": ""},
    {"name": "Library or Framework", "image_url": ""},
    {"name": "Property", "image_url": ""},
    {"name": "Data Type", "image_url": ""}
]

mmc_series_types_list = [
    {"name": "Game", "image_url": ""},
    {"name": "Mode", "image_url": ""},
    {"name": "Character", "image_url": ""},
    {"name": "Mechanic", "image_url": "https://www.pngall.com/wp-content/uploads/5/Game-Controller-PNG-Clipart.png"},
    {"name": "Level", "image_url": "https://www.shutterstock.com/image-vector/2d-arcade-game-level-cartoon-260nw-2259956823.jpg"},
    {"name": "Level Element", "image_url": "https://i.pinimg.com/564x/6e/e9/b5/6ee9b5fdd1f67fbac5fd80445be55245.jpg"},
    {"name": "Enemy Element", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyFefeRiOb3lbMSFGyX6SGFnRD39v7GOr-mg&s"},
    {"name": "Power Up", "image_url": "https://static.vecteezy.com/system/resources/previews/026/973/044/non_2x/3d-icon-video-games-rendered-isolated-on-the-transparent-background-power-up-icon-for-your-design-png.png"},
    {"name": "Property", "image_url": ""},
    {"name": "", "image_url": ""},
]


def add_types():
    collections_to_types = {
        "Super Mario Bros.": smb_types_list,
        "Watership Down": wd_types_list,
        "Chinese Characters": chinese_characters_types_list,
        "Programming Technologies": programming_technology_types_list,
        "Mega Man Classic Series": mmc_series_types_list,
    }

    for collection_name, types_list in collections_to_types.items():
        collection_query = db.session.query(Collections).filter(Collections.name == collection_name).first()

        if not collection_query:
            print(f"Collection '{collection_name}' not found.")
            continue

        for type_data in types_list:
            if db.session.query(Types).filter(Types.name == type_data["name"]).first():
                continue

            new_type = Types(
                type_data["name"],
                "example_description",
                type_data["image_url"],
                type_data.get("color", "#cccccc"),
                None
            )

            new_type.collection_id = collection_query.collection_id

            db.session.add(new_type)

    db.session.commit()