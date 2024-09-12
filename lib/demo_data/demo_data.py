import sys

from lib.demo_data.game_demo_data import add_games


def run_demo_data():
    if len(sys.argv) > 1 and sys.argv[1] == "demo-data":
        print("Creating Demo Data...")
        add_games()