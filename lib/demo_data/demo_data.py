import sys

from lib.demo_data.add_game_elements import add_game_elements
from lib.demo_data.game_element_seed_data import levels_list, enemies_list
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