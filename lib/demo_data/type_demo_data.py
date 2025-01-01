from db import db

from models.types import Types

types_list = ["Mechanic", "Level", "Level Element", "Enemy Element", "Power Up"]

def add_types():
    for index, name in enumerate(types_list):
        if not db.session.query(Types).filter(Types.name == name).first():

            new_type = Types(name, "example_description", "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSyFefeRiOb3lbMSFGyX6SGFnRD39v7GOr-mg&s", "#cccccc", "#444444", "dddddd")

            db.session.add(new_type)
            
    db.session.commit()