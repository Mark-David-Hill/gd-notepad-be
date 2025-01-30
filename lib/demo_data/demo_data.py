import sys
from db import db

from models.relationships import Relationships

from lib.demo_data.watership_down_seed_data import books_list, characters_list
from lib.demo_data.item_seed_data import levels_list, enemies_list, level_elements, power_ups, mechanics
from lib.demo_data.relationship_demo_data import add_relationships
from lib.demo_data.color_scheme_demo_data import add_color_schemes
from lib.demo_data.collection_demo_data import add_collections
from lib.demo_data.user_demo_data import add_users
from lib.demo_data.type_demo_data import add_types
from lib.demo_data.item_demo_data import add_items

def run_demo_data():
    if len(sys.argv) > 1 and sys.argv[1] == "demo-data":
        print("Creating Demo Data...")
        add_color_schemes()
        add_users()
        add_collections()
        add_types()
        add_items("Super Mario Bros.", "Level", levels_list)
        add_items("Super Mario Bros.", "Enemy Element", enemies_list)
        add_items("Super Mario Bros.", "Level Element", level_elements)
        add_items("Super Mario Bros.", "Power Up", power_ups)
        add_items("Super Mario Bros.", "Mechanic", mechanics)
        add_items("Watership Down", "Book", books_list)
        add_items("Watership Down", "Character", characters_list)

        relationships_query = db.session.query(Relationships).all()

        if not relationships_query:
            add_relationships(levels_list)
            add_relationships(enemies_list)
            add_relationships(level_elements)
            add_relationships(power_ups)
            add_relationships(mechanics)