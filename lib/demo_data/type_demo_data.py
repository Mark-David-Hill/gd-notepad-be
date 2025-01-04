from db import db
from models.types import Types

types_list = [
    {"name": "Mechanic", "image_url": "https://www.pngall.com/wp-content/uploads/5/Game-Controller-PNG-Clipart.png"},
    {"name": "Level", "image_url": "https://www.shutterstock.com/image-vector/2d-arcade-game-level-cartoon-260nw-2259956823.jpg"},
    {"name": "Level Element", "image_url": "https://i.pinimg.com/564x/6e/e9/b5/6ee9b5fdd1f67fbac5fd80445be55245.jpg"},
    {"name": "Enemy Element", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyFefeRiOb3lbMSFGyX6SGFnRD39v7GOr-mg&s"},
    {"name": "Power Up", "image_url": "https://static.vecteezy.com/system/resources/previews/026/973/044/non_2x/3d-icon-video-games-rendered-isolated-on-the-transparent-background-power-up-icon-for-your-design-png.png"}
]

def add_types():
    for type in types_list:
        if not db.session.query(Types).filter(Types.name == type["name"]).first():
            new_type = Types(
                type["name"],
                "example_description",
                type["image_url"],
                "#cccccc",
            )
            db.session.add(new_type)
    
    db.session.commit()
