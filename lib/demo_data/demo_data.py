import sys

from lib.demo_data.game_element_demo_data import add_game_elements
from lib.demo_data.game_element_seed_data import levels_list, enemies_list, level_elements, power_ups, mechanics
from lib.demo_data.relationship_demo_data import add_relationships
from lib.demo_data.game_demo_data import add_games
from lib.demo_data.type_demo_data import add_types
from lib.demo_data.user_demo_data import add_users

def run_demo_data():
    if len(sys.argv) > 1 and sys.argv[1] == "demo-data":
        print("Creating Demo Data...")
        add_users()
        add_games()
        add_types()
        add_game_elements("Super Mario Bros.", "Level", levels_list)
        add_game_elements("Super Mario Bros.", "Enemy Element", enemies_list)
        add_game_elements("Super Mario Bros.", "Level Element", level_elements)
        add_game_elements("Super Mario Bros.", "Power Up", power_ups)
        add_game_elements("Super Mario Bros.", "Mechanic", mechanics)
        add_relationships(levels_list)
        add_relationships(enemies_list)
        add_relationships(level_elements)
        add_relationships(power_ups)
        add_relationships(mechanics)