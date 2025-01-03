from db import db
from models.types import Types

types_list = [
    {"name": "Mechanic", "image_url": "path_to_mechanic_image.jpg"},
    {"name": "Level", "image_url": "path_to_level_image.jpg"},
    {"name": "Level Element", "image_url": "path_to_level_element_image.jpg"},
    {"name": "Enemy Element", "image_url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyFefeRiOb3lbMSFGyX6SGFnRD39v7GOr-mg&s"},
    {"name": "Power Up", "image_url": "path_to_power_up_image.jpg"}
]

def add_types():
    for type in types_list:
        if not db.session.query(Types).filter(Types.name == type["name"]).first():
            new_type = Types(
                type["name"],
                "example_description",
                type["image_url"],
                "#cccccc",
                "#444444",
                "dddddd"
            )
            db.session.add(new_type)
    
    db.session.commit()
