import sys

from lib.demo_data.game_demo_data import add_games
from lib.demo_data.type_demo_data import add_types
from lib.demo_data.user_demo_data import add_users
# from lib.demo_data.smb_demo_data.smb_enemy_demo_data import add_enemies


def run_demo_data():
    if len(sys.argv) > 1 and sys.argv[1] == "demo-data":
        print("Creating Demo Data...")
        add_users()
        add_games()
        add_types()
        # add_enemies()