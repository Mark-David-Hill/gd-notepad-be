from db import db

from models.types import Types

types_list = ["Mechanic", "Level", "Level Element", "Enemy Element", "Power Up", "Upgrade", "Economy"]

def add_types():
    for index, name in enumerate(types_list):
        if not db.session.query(Types).filter(Types.name == name).first():

            new_type = Types(name, "example_description")

            db.session.add(new_type)
            
    db.session.commit()